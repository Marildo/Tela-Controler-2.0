from flask import request
from telacore.decorators import http_response
from telacore.exceptions import EntityNotFound
from telacore.utils import CNPJUtil
from webargs.flaskparser import parser

from controller import BaseController, UserController, valide_token
from controller.schemas import EmpresaSchema
from controller.validations.company_validations import CREATE_COMPANY_ARGS, UPDATE_COMPANY_ARGS
from model.entities import Empresa
from model.repository import EmpresaRepository
from services import Manager


class CompanyController(BaseController):

    def __init__(self):
        super().__init__()
        self.__schema = EmpresaSchema()

    @valide_token
    @http_response
    def create(self):
        args = parser.parse(CREATE_COMPANY_ARGS, request, location='json')

        cnpj = CNPJUtil.decode(args['codigo'])
        data = Manager.find_company(cnpj)
        if not data:
            raise EntityNotFound('Empresa não localizada')

        token = UserController().create_user_and_login(cnpj, args)

        empresa = Empresa()
        empresa.nome = data['razao_social']
        empresa.fantasia = data['nome_fantasia']
        empresa.cnpj = data['cnpj']
        empresa.cnae = data['cnae']
        empresa.ibge = data['ibge']
        empresa.uf = data['uf']
        empresa.cep = data['cep']
        empresa.logradouro = data['logradouro']
        empresa.numero = data['numero']
        empresa.complemento = data['complemento']
        empresa.bairro = data['bairro']
        empresa.fone = data['telefone']
        empresa.email = data['email']

        repository = EmpresaRepository(cnpj)
        repository.save(empresa)

        company = self.__schema.dump(empresa)

        data = {
            'token': token,
            'company': company
        }

        return data, 201

    @valide_token
    @http_response
    def read(self):
        repository = EmpresaRepository(self.cnpj)
        data = repository.find()
        data = self.__schema.dump(data)
        return data, 200

    @valide_token
    @http_response
    def update(self, _id):
        args = parser.parse(UPDATE_COMPANY_ARGS, request, location='json')
        del args['id']
        repository = EmpresaRepository(self.cnpj)
        repository.update(Empresa, _id, args)
        return {'id': _id}, 200
