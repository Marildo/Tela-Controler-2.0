from typing import Dict

from flask import request
from telacore.decorators import http_response
from telacore.utils import SecurityUtil
from webargs.flaskparser import parser

from controller import BaseController
from controller.auth_controller import valide_token
from controller.schemas import UsuarioSchema
from controller.validations.user_validations import CREATE_USER_ARGS
from model.entities import Usuario
from model.repository import UsuarioRepository
from services import AuthService


class UserController(BaseController):

    def __init__(self) -> None:
        super().__init__()
        self.__user_schema = UsuarioSchema()

    @valide_token
    @http_response
    def create(self):
        args = parser.parse(CREATE_USER_ARGS, request, location='json')
        user = Usuario(email=args['email'], nome=args['nome'], password=args['password'])
        data = self.__save_user(self.cnpj, user)
        return data, 201

    def create_user_and_login(self, cnpj, args) -> str:
        email = args['email']
        nome = args['nome']
        password = SecurityUtil.hash(args['password'])

        user = Usuario(email=email, nome=nome, password=password)
        data = self.__save_user(cnpj, user)
        token = AuthService().encode(cnpj, data)
        return token

    def __save_user(self, cnpj: str, user: Usuario) -> Dict:
        repository = UsuarioRepository(cnpj)
        repository.save(user)
        data = self.__user_schema.dump(user)
        return data
