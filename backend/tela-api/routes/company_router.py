from datetime import datetime

from flask import request
from flask_restful import Resource

from controller import valide_token, CompanyController


class CompanyRouter(Resource):

    def __init__(self):
        self.__controller = CompanyController()

    @valide_token
    def get(self):
        s = 'ffffgfgfg'
        da = {'Eu sou uma empresa muito legal': str(datetime.now())}
        x = da
        p = request.payload
        print(p)
        return p

    def post(self):
        return self.__controller.create()
