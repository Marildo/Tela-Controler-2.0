from flask import Blueprint

from controller import UserController

name = 'UserRouter'
user_router = Blueprint(name=name, import_name=name, url_prefix='/usuario')


@user_router.route('', methods=['POST'])
def post():
    return UserController().create()
