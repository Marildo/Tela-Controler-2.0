from flask import Blueprint
from telacore.decorators import http_response

from app.proxy import RequestProxy
from controller import CompanyController
from controller.validations.company_validations import CREATE_COMPANY_ARGS

name = 'CompanyRouter'
company_router = Blueprint(name=name, import_name=name, url_prefix='/empresa')


@company_router.route('', methods=['POST'])
@http_response
def post():
    proxy = RequestProxy()
    args = proxy.validate_args(CREATE_COMPANY_ARGS)
    controller = CompanyController()
    controller.initilize(None)
    return controller.create(args)


@company_router.route('', methods=['GET'])
@http_response
def get():
    return CompanyController().read()


@company_router.route('<int:_id>', methods=['PUT'])
@http_response
def put(_id: int):
    return CompanyController().update(_id)
