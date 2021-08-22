from enum import Enum
from typing import Dict

from flask import request
from telacore.models import Credential
from webargs.flaskparser import parser

from services import AuthService


class Location(Enum):
    QUERY = 'querystring'
    JSON = 'json'
    FORM = 'form'
    HEADERS = 'headers'
    COOKIES = 'cookies'
    FILES = 'files'


class RequestProxy:

    def __init__(self):
        pass

    def validate_credential(self) -> Credential:
        headers = request.headers
        assert 'Authorization' in headers, 'Token not found'
        token = headers['Authorization']
        return self.__check_token(token)

    def validate_args(self, validations: Dict, location: Location = Location.JSON) -> Dict:
        args = parser.parse(validations, request, location=location.value)
        return args

    @staticmethod
    def __check_token(token: str) -> Credential:
        token_clear = token.replace('Bearer ', '')
        assert len(token_clear) > 5, 'Token Inválido'
        auth_service = AuthService()
        return auth_service.decode(token_clear)
