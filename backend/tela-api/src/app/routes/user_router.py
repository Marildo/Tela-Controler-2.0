from typing import Tuple

from flask import Blueprint
from telacore.decorators import http_response

from app.routes.proxy import RequestProxy
from app.routes.validators.user_validations import CREATE_USER_ARGS, UPDATE_USER_ARGS, CHANGE_PASSWORD_USER_ARGS
from src.controller import UserController

name = 'UserRouter'
user_router = Blueprint(name=name, import_name=name, url_prefix='/usuarios')


@user_router.route('', methods=['GET'])
@http_response
def get():
    controller, _ = __get_controller()
    return controller.read_all_and_dump()


@user_router.route('<int:_id>', methods=['GET'])
@http_response
def get_by_id(_id: int):
    controller, _ = __get_controller()
    return controller.read_by_id_and_dump(_id)


@user_router.route('', methods=['POST'])
@http_response
def post():
    controller, proxy = __get_controller()
    args = proxy.validate_args(CREATE_USER_ARGS)
    return controller.create(args)


@user_router.route('<int:_id>', methods=['PUT'])
@http_response
def put(_id: int):
    controller, proxy = __get_controller()
    args = proxy.validate_args(UPDATE_USER_ARGS)
    return controller.update(_id, args)


@user_router.route('<int:_id>', methods=['DELETE'])
@http_response
def delete(_id: int):
    controller, _ = __get_controller()
    return controller.delete_and_dump(_id)


@user_router.route('password/<int:_id>', methods=['PATCH'])
@http_response
def change_password(_id: int):
    controller, proxy = __get_controller()
    args = proxy.validate_args(CHANGE_PASSWORD_USER_ARGS)
    return controller.change_password(_id, args)


def __get_controller() -> Tuple[UserController, RequestProxy]:
    proxy = RequestProxy()
    cred = proxy.validate_credential()
    controller = UserController()
    controller.initialize(cred)
    return controller, proxy
