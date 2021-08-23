from flask import Blueprint
from telacore.decorators import http_response

from app.proxy import RequestProxy
from app.proxy.validations.user_validations import CREATE_USER_ARGS
from controller import UserController

name = 'UserRouter'
user_router = Blueprint(name=name, import_name=name, url_prefix='/usuario')


@user_router.route('', methods=['POST'])
@http_response
def post():
    proxy = RequestProxy()
    credential = proxy.validate_credential()
    args = proxy.validate_args(CREATE_USER_ARGS)
    controller = UserController()
    controller.initialize(credential)
    return controller.create(args)
