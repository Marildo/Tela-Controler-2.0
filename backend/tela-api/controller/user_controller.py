from typing import Dict

from flask import request
from telacore.decorators import http_response
from telacore.exceptions import EntityNotFound
from telacore.utils import SecurityUtil
from webargs.flaskparser import parser

from controller.validations.user_validations import CREATE_USER_ARGS
from model.entities import Usuario
from model.repository import UsuarioRepository
from model.schema import UsuarioSchema


class UserController:

    def __init__(self) -> None:
        self.__user_schema = UsuarioSchema()

    @http_response
    def create(self):
        args = parser.parse(CREATE_USER_ARGS, request, location='json')
        password = SecurityUtil.hash(args['password'])
        cnpj = request.cnpj

        new_user = Usuario(email=args['email'], nome=args['nome'], password=password)
        data = self.save_user(cnpj, new_user)
        return data, 201

    def find_for_login(self, cnpj, email, password)-> Dict:
        repository = UsuarioRepository(cnpj)
        user = repository.find_by_email(email)
        if user and user.password == SecurityUtil.hash(password):
            return self.__user_schema.dump(user)

        raise EntityNotFound('Senha ou email incorretos')

    def save_user(self, cnpj: str, user: Usuario) -> Dict:
        repository = UsuarioRepository(cnpj)
        repository.save(user)
        data = self.__user_schema.dump(user)
        return data
