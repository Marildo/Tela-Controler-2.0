from flask_restful import Resource

from controller import AuthContoller
from services import provider_services


class LoginRouter(Resource):

    def __init__(self):
        self.__authController = AuthContoller(provider_services.auth_service)

    def post(self):
        return self.__authController.login()
