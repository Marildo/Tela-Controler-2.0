from flask_restful import Resource

from controller import login


class LoginRouter(Resource):

    @staticmethod
    def post():
        return login()
