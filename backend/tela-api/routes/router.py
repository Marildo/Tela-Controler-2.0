from flask_restful import Api

from .auth_router import LoginRouter
from .company_router import CompanyRouter
from .index_router import IndexRouter
from .user_router import UserRouter


class AppRouter:
    def __init__(self, api: Api):
        self.__api: Api = api

    def load(self):
        api = self.__api
        api.add_resource(IndexRouter, '/')
        api.add_resource(LoginRouter, '/login')
        api.add_resource(CompanyRouter, '/empresa')
        api.add_resource(UserRouter, '/usuario')
