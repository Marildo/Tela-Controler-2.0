from functools import wraps

from flask import request

from controller import AuthContoller
from services import provider_services


def valide_token(f):
    @wraps(f)
    def inner(*args, **kwargs):
        headers = request.headers
        token = headers['Authorization']

        auth = AuthContoller(provider_services.auth_service)
        payload = auth.check_token(token)
        request.payload = payload

        return f(*args, **kwargs)

    return inner
