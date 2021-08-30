from typing import Tuple

from flask import Blueprint
from telacore.decorators import http_response

from src.app.proxy import RequestProxy
from src.app.validations.company_validations import CREATE_COMPANY_ARGS, UPDATE_COMPANY_ARGS
from src.controller import CompanyController

name = 'CompanyRouter'
company_router = Blueprint(name=name, import_name=name, url_prefix='/empresa')


@company_router.route('', methods=['POST'])
@http_response
def post():
    proxy = RequestProxy()
    args = proxy.validate_args(CREATE_COMPANY_ARGS)
    controller = CompanyController()
    controller.initialize(None)
    return controller.create(args)


@company_router.route('/<int:_id>', methods=['GET'])
@http_response
def get(_id: int):
    controller, _ = __get_controller()
    return controller.read_by_id_and_dump(_id)


@company_router.route('/<int:_id>', methods=['PUT'])
@http_response
def put(_id: int):
    controller, proxy = __get_controller()
    args = proxy.validate_args(UPDATE_COMPANY_ARGS)
    return controller.update_and_dump(_id, args)


def __get_controller() -> Tuple[CompanyController, RequestProxy]:
    proxy = RequestProxy()
    cred = proxy.validate_credential()
    controller = CompanyController()
    controller.initialize(cred)
    return controller, proxy
