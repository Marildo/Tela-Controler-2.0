from flask_restful import Resource

from controller import valide_token, CompanyController


class CompanyRouter(Resource):

    def __init__(self):
        self.__controller = CompanyController()

    def post(self):
        return self.__controller.create()

    @valide_token
    def get(self):
        return self.__controller.find()

    @valide_token
    def put(self):
        return self.__controller.update()
