from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from .routes import IndexRouter
from .routes import LoginRouter
from .routes import UserRouter
from .routes import company_router
from .routes import unity_router


class TelaAPP:
    def __init__(self):
        self.__app = Flask('Tela-API')
        self.__config_cors()
        self.__config_routes(self.__app)

    def __config_routes(self, app: Flask):
        api = Api(self.__app)
        api.add_resource(IndexRouter, '/')
        api.add_resource(LoginRouter, '/login')

        api.add_resource(UserRouter, '/usuario')

        app.register_blueprint(unity_router)
        app.register_blueprint(company_router)

    def __config_cors(self):
        CORS(self.__app,
             resources={
                 r"*": {
                     "origins": "*"
                 }
             })

    @property
    def app(self):
        return self.__app
