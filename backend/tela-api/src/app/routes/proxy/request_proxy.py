from enum import Enum
from typing import Dict

from flask import request
from telacore.exceptions import UnauthorizationException
from telacore.models import Credential
from webargs.flaskparser import parser

from src.services import AuthService


class Location(Enum):
    QUERY = 'querystring'
    JSON = 'json'
    FORM = 'form'
    HEADERS = 'headers'
    COOKIES = 'cookies'
    FILES = 'files'


class RequestProxy:

    def validate_credential(self) -> Credential:
        try:
            headers = request.headers
            assert 'Authorization' in headers, 'Token not found'
            token = headers['Authorization']
            credential = self.__check_token(token)
        except Exception as error:
            raise UnauthorizationException(401, error.args[0])

        self.check_resource(credential.permissoes)
        return credential

    def validate_args(self, validations: Dict, location: Location = Location.JSON) -> Dict:
        args = parser.parse(validations, request, location=location.value)
        return args

    def check_resource(self, permissoes):
        error = UnauthorizationException(403, 'Operation not allowed for this user')

        resource = request.url_rule.rule.split('/')[1].split('_')[0]
        permissions = list(filter(lambda x: x.get('recurso') == resource, permissoes))

        if not permissions:
            raise error

        map_method = {
            'POST': 'c',
            'GET': 'r',
            'PUT': 'u',
            'PATCH': 'u',
            'DELETE': 'd'
        }
        permissions = permissions[0]
        method = map_method.get(request.method)
        allowed = permissions.get(method)
        if not allowed:
            raise error

    @staticmethod
    def __check_token(token: str) -> Credential:
        token_clear = token.replace('Bearer ', '')
        assert len(token_clear) > 5, 'Token Inválido'
        auth_service = AuthService()
        return auth_service.decode(token_clear)
