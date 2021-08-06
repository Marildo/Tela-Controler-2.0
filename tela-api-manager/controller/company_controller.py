from flask import request
from webargs.flaskparser import parser

from decorators import http_response
from exceptions import EntityNotFound
from model.config import DBConfig
from model.entities import Empresa
from model.repository import EmpresaRepository
from model.schema import EmpresaSchema
from services import search_from_cnpj
from controller.validations import BY_CNPJ
from utils import str_br_to_date
from brutils import cnpj as lib_cnpj


class CompanyController:

    def __init__(self) -> None:
        config = DBConfig()
        self.__repository = EmpresaRepository(config)
        self.__empresa_schema = EmpresaSchema()

    @http_response
    def load_by_cnpj(self):
        args = parser.parse(BY_CNPJ, request, location='view_args')
        cnpj = args['cnpj']
        cnpj = str(cnpj).rjust(14, '0')

        cnpj_with_mask = lib_cnpj.display(cnpj)
        company = self.__repository.find_by_cnpj(cnpj_with_mask)
        if company:
            return self.__empresa_schema.dump(company), 200

        company = search_from_cnpj(cnpj)
        if company['status'] == 'ERROR':
            raise EntityNotFound(company['message'])
        else:
            self.__save(company)
            company = self.__repository.find_by_cnpj(cnpj_with_mask)
            return self.__empresa_schema.dump(company), 200

    def __save(self, company):
        empresa = Empresa()
        empresa.cnpj = company['cnpj']
        empresa.razao_social = company['nome']
        empresa.nome_fantasia = company['fantasia']
        empresa.abertura = str_br_to_date(company['abertura'])
        empresa.data_situacao = str_br_to_date(company['data_situacao'])
        empresa.cnae = company['atividade_principal'][0]['code']
        empresa.logradouro = company['logradouro']
        empresa.numero = company['numero']
        empresa.complemento = company['complemento']
        empresa.bairro = company['bairro']
        empresa.cep = company['cep']
        empresa.municipio = company['municipio']
        empresa.uf = company['uf']
        empresa.telefone = company['telefone']
        empresa.email = company['email']
        empresa.situacao = company['situacao'] == 'ATIVA'
        self.__repository.save(empresa)
        return  empresa
