from flask_restful import Resource

from controller import AuthContoller
from services import JWTService


class LoginRouter(Resource):

    def __init__(self):
        self.__authController = AuthContoller(JWTService())

    def post(self):
        return self.__authController.login()

    def get(self):
        return self.__authController.check_token()
