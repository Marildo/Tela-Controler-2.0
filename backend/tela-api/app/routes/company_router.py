from flask import Blueprint

from controller import CompanyController, valide_token

name = 'CompanyRouter'
company_router = Blueprint(name=name, import_name=name, url_prefix='/empresa')


@company_router.route('/', methods=['POST'])
def post():
    return CompanyController().create()


@company_router.route('/', methods=['GET'])
def get():
    return CompanyController().read()


@company_router.route('/<int:_id>', methods=['PUT'])
def put(_id: int):
    return CompanyController().update(_id)
