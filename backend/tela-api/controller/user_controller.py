from typing import Dict

from flask import request
from telacore.decorators import http_response
from telacore.exceptions import EntityNotFound
from telacore.utils import SecurityUtil
from webargs.flaskparser import parser

from controller.validations.user_validations import CREATE_USER_ARGS
from model.entities import Usuario
from model.repository import UsuarioRepository
from model.schemas import UsuarioSchema
from services import AuthService


class UserController:

    def __init__(self) -> None:
        self.__user_schema = UsuarioSchema()

    @http_response
    def create(self):
        args = parser.parse(CREATE_USER_ARGS, request, location='json')
        cnpj = request.cnpj
        data = self.create_user_and_login(cnpj, args)
        return data, 201

    def create_user_and_login(self, cnpj, args) -> str:
        email = args['email']
        nome = args['nome']
        password = SecurityUtil.hash(args['password'])

        user = Usuario(email=email, nome=nome, password=password)
        data = self.__save_user(cnpj, user)
        token = AuthService().encode(cnpj, data)
        return token

    def find_for_login(self, cnpj, email, password) -> Dict:
        repository = UsuarioRepository(cnpj)
        user = repository.find_by_email(email)
        if user and user.password == SecurityUtil.hash(password):
            return self.__user_schema.dump(user)

        raise EntityNotFound('Senha ou email incorretos')

    def __save_user(self, cnpj: str, user: Usuario) -> Dict:
        repository = UsuarioRepository(cnpj)
        repository.save(user)
        data = self.__user_schema.dump(user)
        return data
