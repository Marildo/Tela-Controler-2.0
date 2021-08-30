from typing import Tuple

from flask import Blueprint
from telacore.decorators import http_response

from src.app.proxy import RequestProxy
from src.app.validations.unity_validations import CREATE_UNITY_ARGS, UPDATE_UNITY_ARGS
from src.controller import UnityController

name = 'UnityRouter'
unity_router = Blueprint(name=name, import_name=name, url_prefix='/unidades')


@unity_router.route('', methods=['GET'])
@http_response
def get():
    controller, _ = __get_controller()
    return controller.read_all_and_dump()


@unity_router.route('<int:_id>', methods=['GET'])
@http_response
def get_by_id(_id: int):
    controller, _ = __get_controller()
    return controller.read_by_id_and_dump(_id)


@unity_router.route('', methods=['POST'])
@http_response
def post():
    controller, proxy = __get_controller()
    args = proxy.validate_args(CREATE_UNITY_ARGS)
    return controller.create(args)


@unity_router.route('<int:_id>', methods=['PUT'])
@http_response
def put(_id: int):
    controller, proxy = __get_controller()
    args = proxy.validate_args(UPDATE_UNITY_ARGS)
    return controller.update(args, _id)


@unity_router.route('<int:_id>', methods=['DELETE'])
@http_response
def delete(_id: int):
    controller, _ = __get_controller()
    return controller.delete(_id)


def __get_controller() -> Tuple[UnityController, RequestProxy]:
    proxy = RequestProxy()
    cred = proxy.validate_credential()
    controller = UnityController()
    controller.initialize(cred)
    return controller, proxy
