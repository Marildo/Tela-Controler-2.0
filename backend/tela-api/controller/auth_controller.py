from functools import wraps
from typing import Dict

from flask import request
from telacore.decorators import http_response
from telacore.exceptions import EntityNotFound
from telacore.models import Credential, TelaResponse
from telacore.utils import CNPJUtil, SecurityUtil
from telacore.utils.logger_util import log_error
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


# TODO - REMOVER
def check_token(token: str) -> Credential:
    token = token.replace('Bearer ', '')
    assert len(token) > 5, 'Token Inválido'
    auth_service = AuthService()
    return auth_service.decode(token)


# TODO - REMOVER
def valide_token(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            headers = request.headers
            assert 'Authorization' in headers, 'Token not found'
            token = headers['Authorization']
            controller = args[0]
            controller.credential = check_token(token)
            return func(*args, **kwargs)
        except Exception as error:
            log_error(error)
            data = {'error': error.args[0]}
            response = TelaResponse(success=False, data=data, code=401)
            return response.get()

    return decorator
