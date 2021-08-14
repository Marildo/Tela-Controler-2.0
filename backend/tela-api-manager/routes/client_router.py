from flask_restful import Resource

from controller.client_controller import ClientController


class ClientRouter(Resource):

    @staticmethod
    def get():
        return ClientController().load()

    @staticmethod
    def post():
        return ClientController().save()
