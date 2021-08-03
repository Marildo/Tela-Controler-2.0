from flask_restful import Resource

from controller.usuario_controller import add_user


class UserRouter(Resource):

    @staticmethod
    def post():
        return add_user()

