from flask_restful import Resource

from controller import UserController


class UserRouter(Resource):

    @staticmethod
    def post():
        return UserController().create()

