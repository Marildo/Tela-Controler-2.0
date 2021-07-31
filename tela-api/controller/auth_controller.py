from functools import wraps

from flask import request
from webargs.flaskparser import parser

from decorators import http_response
from services import provider_services
from validations import user_args


@http_response
def login():
    args = parser.parse(user_args, request, location='json')
    token = provider_services.auth_service.encode(args)
    return {'token': token}, 2902


def check_token(token: str):
    token = token.replace('Bearer ', '')
    payload = provider_services.auth_service.decode(token)
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
