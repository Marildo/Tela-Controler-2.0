from typing import Tuple

from flask import Blueprint
from telacore.decorators import http_response

from src.app.routes.proxy import RequestProxy
from src.app.routes.validators.order_validations import CREATE_ORDER_ARGS, UPDATE_ORDER_ARGS
from src.controller import OrderController

order_router = Blueprint(name='OrderRouter', import_name='OrderRouter', url_prefix='/pedidos')


@order_router.route('', methods=['GET'])
@http_response
def get():
    controller, _ = __get_controller()
    return controller.read_all_and_dump()


@order_router.route('<int:_id>', methods=['GET'])
@http_response
def get_by_id(_id: int):
    controller, _ = __get_controller()
    return controller.read_by_id_and_dump(_id)


@order_router.route('', methods=['POST'])
@http_response
def __post():
    controller, proxy = __get_controller()
    args = proxy.validate_args(CREATE_ORDER_ARGS)
    return controller.create_and_dump(args)


@order_router.route('<int:_id>', methods=['PUT'])
@http_response
def put(_id: int):
    controller, proxy = __get_controller()
    args = proxy.validate_args(UPDATE_ORDER_ARGS)
    return controller.update_and_dump(_id, args)


def __get_controller() -> Tuple[OrderController, RequestProxy]:
    proxy = RequestProxy()
    cred = proxy.validate_credential()
    controller = OrderController()
    controller.initialize(cred)
    return controller, proxy
