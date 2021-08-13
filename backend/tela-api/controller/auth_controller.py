from functools import wraps

from flask import request
from telacore.models.response import Response
from telacore.decorators import http_response
from telacore.utils.logger_util import log_error
from webargs.flaskparser import parser

from controller.user_controller import UserController
from controller.validations import LOGIN_ARGS
from services import AuthService


@http_response
def login():
    args = parser.parse(LOGIN_ARGS, request, location='json')
    user = UserController().find_for_login(email=args['email'], password=args['password'])
    token = AuthService().encode(user)
    return {'token': token}, 200


def check_token(token: str):
    token = token.replace('Bearer ', '')
    assert len(token) > 5, 'Token Inválido'
    auth_service = AuthService()
    payload = auth_service.decode(token)
    return payload


def valide_token(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            headers = request.headers
            token = headers['Authorization']

            payload = check_token(token)
            request.payload = payload
            func(*args, **kwargs)
        except Exception as error:
            log_error(error)
            data = {'error': error.args[0]}
            response = Response(success=False, data=data, code=401)
            return response.get()

    return decorator
