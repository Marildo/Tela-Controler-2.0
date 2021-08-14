from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from app.routes.auth_router import LoginRouter
from app.routes.company_router import CompanyRouter
from app.routes.index_router import IndexRouter
from app.routes.user_router import UserRouter


class TelaAPP:
    def __init__(self):
        self.__app = Flask('Tela-API')
        self.__config_cors()
        self.__config_routes()

    def __config_routes(self):
        api = Api(self.__app)
        api.add_resource(IndexRouter, '/')
        api.add_resource(LoginRouter, '/login')
        api.add_resource(CompanyRouter, '/empresa')
        api.add_resource(UserRouter, '/usuario')

    def __config_cors(self):
        CORS(self.__app,
             resources={r"*":
                            {"origins": "*"}
                        }
             )

    @property
    def app(self):
        return self.__app
