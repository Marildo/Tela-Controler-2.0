from functools import wraps

from flask import request
from webargs.flaskparser import parser

from controller.user_controller import UserController
from telacore.decorators import http_response
from services import AuthService
from controller.validations import LOGIN_ARGS


@http_response
def login():
    args = parser.parse(LOGIN_ARGS, request, location='json')
    user = UserController().find_for_login(email=args['email'], password=args['password'])
    token = AuthService().encode(user)
    return {'token': token}, 200


def check_token(token: str):
    token = token.replace('Bearer ', '')
    payload = AuthService.decode(token)
    return payload


def valide_token(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        headers = request.headers
        token = headers['Authorization']
        payload = check_token(token)
        request.payload = payload
        return func(*args, **kwargs)

    return decorator
