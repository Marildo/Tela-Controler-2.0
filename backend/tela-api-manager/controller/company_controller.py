from flask import request
from telacore.utils import date_util, cnpj_util
from webargs.flaskparser import parser

from controller.validations import CNPJ
from decorators import http_response
from exceptions import EntityNotFound
from model.entities import Empresa
from model.repository import EmpresaRepository
from model.schema import EmpresaSchema
from services import search_from_cnpj


class CompanyController:

    def __init__(self) -> None:
        self.__repository = EmpresaRepository()
        self.__empresa_schema = EmpresaSchema()

    @http_response
    def load_by_cnpj(self):
        args = parser.parse(CNPJ, request, location='view_args')
        cnpj = args['cnpj']
        cnpj = str(cnpj).rjust(14, '0')

        company = self.find_and_save(cnpj)
        return self.__empresa_schema.dump(company), 200

    def find_and_save(self, cnpj) -> Empresa:
        cnpj_with_mask = cnpj_util.mask(cnpj)
        company = self.__repository.find_by_cnpj(cnpj_with_mask)
        if company:
            return company

        company = search_from_cnpj(cnpj)
        if company['status'] == 'ERROR':
            raise EntityNotFound(company['message'])
        else:
            self.__save(company)
            return self.__repository.find_by_cnpj(cnpj_with_mask)

    def __save(self, company):
        empresa = Empresa()
        empresa.cnpj = company['cnpj']
        empresa.razao_social = company['nome']
        empresa.nome_fantasia = company['fantasia']
        empresa.abertura = date_util.br_parse_date(company['abertura'])
        empresa.data_situacao = date_util.br_parse_date(company['data_situacao'])
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
        return empresa
