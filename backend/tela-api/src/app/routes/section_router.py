from typing import Tuple

from flask import Blueprint
from telacore.decorators import http_response

from app.routes.proxy import RequestProxy
from app.routes.validators.section_validations import CREATE_SECTION_ARGS, UPDATE_SECTION_ARGS
from src.controller import SectionController

name = 'SectionRouter'
resource  = '/setores'
section_router = Blueprint(name=name, import_name=name, url_prefix= resource)


@section_router.route('', methods=['GET'])
@http_response
def get():
    controller, _ = __get_controller()
    return controller.read_all_and_dump()


@section_router.route('<int:_id>', methods=['GET'])
@http_response
def get_by_id(_id: int):
    controller, _ = __get_controller()
    return controller.read_by_id_and_dump(_id)


@section_router.route('', methods=['POST'])
@http_response
def post():
    controller, proxy = __get_controller()
    args = proxy.validate_args(CREATE_SECTION_ARGS)
    return controller.create(args)


@section_router.route('<int:_id>', methods=['PUT'])
@http_response
def put(_id: int):
    controller, proxy = __get_controller()
    args = proxy.validate_args(UPDATE_SECTION_ARGS)
    return controller.update_and_dump(_id, args)


@section_router.route('<int:_id>', methods=['DELETE'])
@http_response
def delete(_id: int):
    controller, _ = __get_controller()
    return controller.delete_and_dump(_id)


def __get_controller() -> Tuple[SectionController, RequestProxy]:
    proxy = RequestProxy()
    cred = proxy.validate_credential()
    controller = SectionController()
    controller.initialize(cred)
    return controller, proxy
