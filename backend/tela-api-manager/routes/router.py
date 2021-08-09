from flask_restful import Api

from .client_router import ClientRouter
from .company_router import CompanyRouter


# TODO - Adiconar algum disposito de segurança
class AppRouter:
    def __init__(self, api: Api):
        self.__api: Api = api

    def load(self):
        api = self.__api
        api.add_resource(CompanyRouter, '/empresa/<cnpj>')
        api.add_resource(ClientRouter, '/cliente/<cnpj>')
