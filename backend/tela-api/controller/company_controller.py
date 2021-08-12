from flask import request
from telacore.decorators import http_response
from telacore.exceptions import EntityNotFound
from telacore.utils import SecurityUtil
from telacore.utils import cnpj_util
from webargs.flaskparser import parser

from controller import UserController
from controller.validations.company_validations import CREATE_COMPANY_ARGS
from model.entities import Usuario
from services import Manager, AuthService


class CompanyController:

    def __init__(self):
        pass

    @http_response
    def create(self):
        args = parser.parse(CREATE_COMPANY_ARGS, request, location='json')

        cnpj = cnpj_util.decode(args['codigo'])
        data = Manager.find_company(cnpj)
        if not data:
            raise EntityNotFound('Empresa não localizada')

        token = self.create_user_and_login(cnpj, args)

        data = {
            'token': token
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
