from typing import Tuple

from flask import Blueprint
from telacore.decorators import http_response

from app.routes.proxy import RequestProxy
from app.routes.validators.resource_validations import CREATE_RESOURCE_ARGS
from src.controller import ResourceController

name = 'ResourceRouter'
resource_router = Blueprint(name=name, import_name=name, url_prefix='/recursos')


@resource_router.route('', methods=['GET'])
@http_response
def get():
    controller, _ = __get_controller()
    return controller.read_all_and_dump()


@resource_router.route('<int:_id>', methods=['GET'])
@http_response
def get_by_id(_id: int):
    controller, _ = __get_controller()
    return controller.read_by_id_and_dump(_id)


@resource_router.route('', methods=['POST'])
@http_response
def post():
    controller, proxy = __get_controller()
    args = proxy.validate_args(CREATE_RESOURCE_ARGS)
    return controller.create(args)


def __get_controller() -> Tuple[ResourceController, RequestProxy]:
    proxy = RequestProxy()
    cred = proxy.validate_credential()
    controller = ResourceController()
    controller.initialize(cred)
    return controller, proxy
