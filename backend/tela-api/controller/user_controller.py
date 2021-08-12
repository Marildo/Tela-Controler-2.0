from hashlib import sha512

from flask import request
from webargs.flaskparser import parser

from telacore.decorators import http_response
from telacore.exceptions import EntityNotFound
from model.config import DBConfig
from model.entities import Usuario
from model.repository import UsuarioRepository
from model.schema import UsuarioSchema
from controller.validations import ADD_USER_ARGS


class UserController:

    def __init__(self) -> None:
        config = DBConfig()
        self.__repository = UsuarioRepository(config)
        self.__user_schema = UsuarioSchema()

    @http_response
    def add(self):
        args = parser.parse(ADD_USER_ARGS, request, location='json')
        password = self.__encode(args['password'])

        new_user = Usuario(email=args['email'], nome=args['nome'], password=password)
        self.__repository.save(new_user)

        data = self.__user_schema.dump(new_user)
        return data, 201

    def find_for_login(self, email, password):
        user = self.__repository.find_by_email(email)
        if user and user.password == self.__encode(password):
            return self.__user_schema.dump(user)

        raise EntityNotFound('Senha ou email incorretos')

    @staticmethod
    def __encode(text: str) -> str:
        return sha512(text.encode('utf-8')).hexdigest()
