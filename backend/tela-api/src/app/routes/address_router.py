from typing import Tuple

from flask import Blueprint
from telacore.decorators import http_response

from src.app.routes.proxy import RequestProxy
from src.app.routes.validators.address_validations import CREATE_ADDRESS_ARGS, UPDATE_ADDRESS_ARGS
from src.controller import AddressController

address_router = Blueprint(name='AddressRouter', import_name='AddressRouter', url_prefix='/enderecos')


@address_router.route('', methods=['GET'])
@http_response
def get():
    controller, _ = __get_controller()
    return controller.read_all_and_dump()


@address_router.route('<int:_id>', methods=['GET'])
@http_response
def get_by_id(_id: int):
    controller, _ = __get_controller()
    return controller.read_by_id_and_dump(_id)


@address_router.route('', methods=['POST'])
@http_response
def post():
    controller, proxy = __get_controller()
    args = proxy.validate_args(CREATE_ADDRESS_ARGS)
    return controller.create_and_dump(args)


@address_router.route('<int:_id>', methods=['PUT'])
@http_response
def put(_id: int):
    controller, proxy = __get_controller()
    args = proxy.validate_args(UPDATE_ADDRESS_ARGS)
    return controller.update_and_dump(_id, args)


@address_router.route('<int:_id>', methods=['DELETE'])
@http_response
def delete(_id: int):
    controller, _ = __get_controller()
    return controller.delete_and_dump(_id)


def __get_controller() -> Tuple[AddressController, RequestProxy]:
    proxy = RequestProxy()
    cred = proxy.validate_credential()
    controller = AddressController()
    controller.initialize(cred)
    return controller, proxy
