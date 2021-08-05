from flask_restful import Resource

from controller import CompanyController


class CompanyRouter(Resource):

    @staticmethod
    def get(cnpj):
        return CompanyController().load_by_cnpj()
