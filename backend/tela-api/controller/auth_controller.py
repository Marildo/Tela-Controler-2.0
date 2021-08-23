from typing import Dict

from flask import request
from telacore.decorators import http_response
from telacore.exceptions import EntityNotFound
from telacore.utils import CNPJUtil, SecurityUtil
from webargs.flaskparser import parser

from controller.schemas import UsuarioSchema
from controller.validations import LOGIN_ARGS
from model.repository import UsuarioRepository
from services import AuthService


@http_response
def login():
    args = parser.parse(LOGIN_ARGS, request, location='json')
    cnpj = CNPJUtil.decode(args['codigo'])
    user = find_for_login(cnpj=cnpj, email=args['email'], password=args['password'])

    token = AuthService().encode(cnpj=cnpj, payload=user)
    return {'token': token}, 200


def find_for_login(cnpj, email, password) -> Dict:
    repository = UsuarioRepository(cnpj)
    user = repository.find_by_email(email)
    if user and user.password == SecurityUtil.hash(password):
        return UsuarioSchema().dump(user)
    raise EntityNotFound('Senha ou email incorretos')
