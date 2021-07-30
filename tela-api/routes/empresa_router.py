from datetime import datetime

from flask_restful import Resource
from flask import request

from decorators import valide_token


class EmpresaRouter(Resource):

    @valide_token
    def get(self):
        s = 'ffffgfgfg'
        da = {'Eu sou uma empresa muito legal': str(datetime.now())}
        x = da
        p = request.payload
        print(p)
        return p
