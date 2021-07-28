from flask import request

from services import IAuth


class AuthContoller:

    def __init__(self, auth_service: IAuth):
        self.__auth_service = auth_service

    def login(self):
        args = request.args
        token = self.__auth_service.encode(args)
        return {'token': token}

    def check_token(self):
        token = request.args['token']
        payload = self.__auth_service.decode(token)
        return payload
