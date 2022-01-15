from typing import Tuple

from flask import Blueprint
from telacore.decorators import http_response

from src.app.routes.proxy import RequestProxy
from src.app.routes.validators.customer_validations import CREATE_CUSTOMER_ARGS, UPDATE_CUSTOMER_ARGS
from src.controller import CustomerController

name = 'CustomerRouter'
customer_router = Blueprint(name=name, import_name=name, url_prefix='/participantes')


@customer_router.route('', methods=['GET'])
@http_response
def get():
    controller, proxy = __get_controller()
    query_page = proxy.query_page()
    return controller.read_all_and_dump(query_page)


@customer_router.route('<int:_id>', methods=['GET'])
@http_response
def get_by_id(_id: int):
    controller, _ = __get_controller()
    return controller.read_by_id_and_dump(_id)


@customer_router.route('', methods=['POST'])
@http_response
def post():
    controller, proxy = __get_controller()
    args = proxy.validate_args(CREATE_CUSTOMER_ARGS)
    return controller.create_and_dump(args)


@customer_router.route('<int:_id>', methods=['PUT'])
@http_response
def put(_id: int):
    controller, proxy = __get_controller()
    args = proxy.validate_args(UPDATE_CUSTOMER_ARGS)
    return controller.update_and_dump(_id, args)


@customer_router.route('<int:_id>', methods=['DELETE'])
@http_response
def delete(_id: int):
    controller, _ = __get_controller()
    return controller.soft_delete_and_dump(_id)

def __get_controller() -> Tuple[CustomerController, RequestProxy]:
    proxy = RequestProxy()
    cred = proxy.validate_credential()
    controller = CustomerController()
    controller.initialize(cred)
    return controller, proxy
