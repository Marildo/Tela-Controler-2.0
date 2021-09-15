from typing import Tuple

from flask import Blueprint
from telacore.decorators import http_response

from src.app.routes.proxy import RequestProxy
from src.app.routes.validators.item_order_validations import CREATE_ITEM_ORDER_ARGS, UPDATE_ITEM_ORDER_ARGS
from src.controller import ItemOrderController

item_order_router = Blueprint(name='ItemOrderRouter', import_name='ItemOrderRouter', url_prefix='/pedidos/item')



@item_order_router.route('', methods=['POST'])
@http_response
def __post():
    controller, proxy = __get_controller()
    args = proxy.validate_args(CREATE_ITEM_ORDER_ARGS)
    return controller.create_and_dump(args)


@item_order_router.route('<int:_id>', methods=['PUT'])
@http_response
def put(_id: int):
    controller, proxy = __get_controller()
    args = proxy.validate_args(UPDATE_ITEM_ORDER_ARGS)
    return controller.update_and_dump(_id, args)


@item_order_router.route('<int:_id>', methods=['DELETE'])
@http_response
def delete(_id: int):
    controller, _ = __get_controller()
    return controller.delete_and_dump(_id)    


def __get_controller() -> Tuple[ItemOrderController, RequestProxy]:
    proxy = RequestProxy()
    cred = proxy.validate_credential()
    controller = ItemOrderController()
    controller.initialize(cred)
    return controller, proxy
