from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from .routes import ClientRouter
from .routes import CompanyRouter


class TelaAPP:
    def __init__(self):
        self.__app = Flask('Tela-API')
        self.__config_cors()
        self.__config_routes()

    def __config_routes(self):
        api = Api(self.__app)
        api.add_resource(CompanyRouter, '/empresa/<cnpj>')
        api.add_resource(ClientRouter, '/cliente/')

    def __config_cors(self):
        CORS(self.__app,
             resources={r"*":
                            {"origins": "*"}
                        }
             )

    @property
    def app(self):
        return self.__app
