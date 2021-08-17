from flask import Flask
from flask_cors import CORS

from .routes import auth_router
from .routes import company_router
from .routes import index_router
from .routes import unity_router
from .routes import user_router


class TelaAPP:
    def __init__(self):
        self.__app = Flask('Tela-API')
        self.__config_cors()
        self.__config_routes(self.__app)

    def __config_routes(self, app: Flask):
        app.register_blueprint(index_router)
        app.register_blueprint(auth_router)
        app.register_blueprint(unity_router)
        app.register_blueprint(user_router)
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
