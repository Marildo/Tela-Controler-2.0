from typing import Tuple

from flask import Blueprint
from telacore.decorators import http_response

from app.routes.proxy import RequestProxy
from app.routes.validators.product_validations import CREATE_PRODUCT_ARGS, UPDATE_PRODUCT_ARGS
from src.controller import ProductController

product_router = Blueprint(name='ProductRouter', import_name='ProductRouter', url_prefix='/produtos')


@product_router.route('', methods=['GET'])
@http_response
def get():
    controller, _ = __get_controller()
    return controller.read_all_and_dump()


@product_router.route('<int:_id>', methods=['GET'])
@http_response
def get_by_id(_id: int):
    controller, _ = __get_controller()
    return controller.read_by_id_and_dump(_id)


@product_router.route('', methods=['POST'])
@http_response
def __post():
    controller, proxy = __get_controller()
    args = proxy.validate_args(CREATE_PRODUCT_ARGS)
    return controller.create(args)


@product_router.route('<int:_id>', methods=['PUT'])
@http_response
def put(_id: int):
    controller, proxy = __get_controller()
    args = proxy.validate_args(UPDATE_PRODUCT_ARGS)
    return controller.update_and_dump(_id, args)


@product_router.route('<int:_id>', methods=['DELETE'])
@http_response
def delete(_id: int):
    controller, _ = __get_controller()
    return controller.delete_and_dump(_id)


def __get_controller() -> Tuple[ProductController, RequestProxy]:
    proxy = RequestProxy()
    cred = proxy.validate_credential()
    controller = ProductController()
    controller.initialize(cred)
    return controller, proxy
