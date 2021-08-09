from controller.client_controller import ClientController
from flask_restful import Resource

 

class ClientRouter(Resource):

    @staticmethod
    def get(cnpj):
        return ClientController().load()

    @staticmethod
    def post(cnpj):
        return ClientController().save()        