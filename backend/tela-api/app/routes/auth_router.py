from flask import Blueprint

from controller import login

name = 'AuthRouter'
auth_router = Blueprint(name=name, import_name=name, url_prefix='/login')


@auth_router.route('', methods=['POST'])
def post():
    return login()
