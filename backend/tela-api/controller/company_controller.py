from flask import request
from telacore.decorators import http_response
from telacore.exceptions import EntityNotFound
from telacore.utils import cnpj_util
from webargs.flaskparser import parser

from controller import UserController
from controller.validations.company_validations import CREATE_COMPANY_ARGS, UPDATE_COMPANY_ARGS
from model.entities import Empresa
from model.repository import EmpresaRepository
from model.schemas import EmpresaSchema
from services import Manager


class CompanyController:

    def __init__(self):
        self.__schema = EmpresaSchema()

    @http_response
    def create(self):
        args = parser.parse(CREATE_COMPANY_ARGS, request, location='json')

        cnpj = cnpj_util.decode(args['codigo'])
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

        return data, 200

    @http_response
    def find(self):
        cnpj = request.credential.cnpj
        repository = EmpresaRepository(cnpj)
        data = repository.find()
        data = self.__schema.dump(data)
        return data, 200

    @http_response
    def update(self):
        args = parser.parse(UPDATE_COMPANY_ARGS, request, location='json')
        return 'ok'
