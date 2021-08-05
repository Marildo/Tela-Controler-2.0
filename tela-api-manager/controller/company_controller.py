from flask import request
from webargs.flaskparser import parser

from decorators import http_response
from exceptions import EntityNotFound
from model.config import DBConfig
from model.repository import EmpresaRepository
from model.schema import EmpresaSchema
from services import search_from_cnpj
from validations import BY_CNPJ


class CompanyController:

    def __init__(self) -> None:
        config = DBConfig()
        self.__repository = EmpresaRepository(config)
        self.__empresa_schema = EmpresaSchema

    @http_response
    def load_by_cnpj(self):
        args = parser.parse(BY_CNPJ, request, location='view_args')
        cnpj = args['cnpj']
        cnpj = str(cnpj).rjust(14, '0')
        company = self.__repository.find_by_cnpj(cnpj)
        if company:
            return self.__empresa_schema.dump(company)

        company = search_from_cnpj(cnpj)

        if company['status'] == 'ERROR':
            raise EntityNotFound(company['message'])

        raise EntityNotFound('Empresa não localiza')

        return company, 200
