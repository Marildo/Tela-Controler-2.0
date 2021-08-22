from flask import Blueprint

from app.proxy import RequestProxy
from controller.validations import product_validations
from controller import ProductController
from telacore.decorators import http_response
product_router = Blueprint(name='ProductRouter', import_name='ProductRouter', url_prefix='/produtos')


@product_router.route('', methods=['GET'])
def __get():
    proxy = RequestProxy()
    proxy.validate_credential()

    return 'Lista de produtos'


@product_router.route('', methods=['POST'])
@http_response
def __post():
    proxy = RequestProxy()
    cred = proxy.validate_credential()
    args = proxy.validate_args(product_validations.PRODUCT_CREATE_ARGS)
    return ProductController(cred).create(args)
