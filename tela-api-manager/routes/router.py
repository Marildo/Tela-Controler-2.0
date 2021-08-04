from flask_restful import Api

from .company_router import CompanyRouter


class AppRouter:
    def __init__(self, api: Api):
        self.__api: Api = api

    def load(self):
        api = self.__api
        api.add_resource(CompanyRouter, '/empresa/<cnpj>')
