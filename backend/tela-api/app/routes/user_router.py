from app.proxy import RequestProxy
from app import proxy
from flask import Blueprint
from telacore.decorators import http_response
from controller import UserController
from controller.validations.user_validations import CREATE_USER_ARGS

name = 'UserRouter'
user_router = Blueprint(name=name, import_name=name, url_prefix='/usuario')


@user_router.route('', methods=['POST'])
@http_response
def post():
    proxy = RequestProxy()
    credential = proxy.validate_credential()
    args = proxy.validate_args(CREATE_USER_ARGS)
    return UserController(credential).create(args)
