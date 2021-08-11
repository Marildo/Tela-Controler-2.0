import datetime

from flask import request
from telacore.decorators import http_response
from telacore.exceptions import EntityNotFound
from telacore.utils import cnpj_util
from webargs.flaskparser import parser

from controller import CompanyController
from controller.validations import CNPJ
from model.entities.cliente import Cliente
from model.repository import ClienteRepository


class ClientController:

    def __init__(self):
        self.__repository = ClienteRepository()

    @http_response
    def load(self):
        arqs = parser.parse(CNPJ, request, location='view_args')
        cnpj = cnpj_util.mask(arqs['cnpj'])

        cliente = self.__repository.find(cnpj)
        if not cliente:
            raise EntityNotFound('Empresa não está cadastrada')

        return {'id': cliente.uuid}, 200

    @http_response
    def save(self):
        arqs = parser.parse(CNPJ, request, location='view_args')
        cnpj = arqs['cnpj']
        cnpj = cnpj_util.mask(cnpj)

        cliente = self.__repository.find(cnpj)
        if cliente:
            cliente.last_token = datetime.datetime.now()
            self.__repository.save(cliente)
            return {'token': cliente.uuid}, 200

        company_controller = CompanyController()
        company = company_controller.find_and_save(cnpj)
        cliente = Cliente()
        cliente.uuid = cnpj_util.encode(cnpj)
        cliente.empresa_id = company.id
        self.__repository.save(cliente)
        return {'token': cliente.uuid}, 201
