from flask import request
from telacore.decorators import http_response
from telacore.exceptions import EntityNotFound
from telacore.utils import SecurityUtil
from telacore.utils import cnpj_util
from webargs.flaskparser import parser

from controller import UserController
from controller.validations.company_validations import CREATE_COMPANY_ARGS
from model.entities import Usuario, Empresa
from model.repository import EmpresaRepository
from model.schemas import EmpresaSchema
from services import Manager, AuthService


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

        token = self.create_user_and_login(cnpj, args)

        empresa = Empresa()
        empresa.nome = data['razao_social']
        empresa.fantasia = data['nome_fantasia']
        empresa.cnpj = data['cnpj']
        empresa.cnae = data['cnae']
        empresa.uf = data['uf']
        empresa.cep = data['cep']
        empresa.logradouro = data['logradouro']
        empresa.numero = data['numero']
        empresa.complemento = data['complemento']
        empresa.bairro = data['bairro']
        empresa.fone = data['telefone']
        empresa.email = data['email']

        #TODO - Buscar cep e salvar ibge

        repository = EmpresaRepository(cnpj)
        repository.save(empresa)

        company = self.__schema.dump(empresa)

        data = {
            'token': token,
            'company': company
        }

        return data, 200

    @staticmethod
    def create_user_and_login(cnpj, args) -> str:
        email = args['email']
        nome = args['nome']
        password = SecurityUtil.hash(args['password'])

        user = Usuario(email=email, nome=nome, password=password)
        user_controller = UserController()
        data = user_controller.save_user(cnpj, user)
        token = AuthService().encode(data)
        return token
