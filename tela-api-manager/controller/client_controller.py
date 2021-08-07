import uuid

from flask import request
from webargs.flaskparser import parser

from controller import CompanyController
from controller.validations import CNPJ
from decorators import http_response
from exceptions import EntityNotFound
from model.entities.cliente import Cliente
from model.repository import ClienteRepository
from utils import CNPJUtil


class ClientController:

    def __init__(self):
        self.__repository = ClienteRepository()

    @http_response
    def load(self):
        arqs = parser.parse(CNPJ, request, location='view_args')
        cnpj = CNPJUtil.mask(arqs['cnpj'])

        cliente = self.__repository.find(cnpj)
        if not cliente:
            raise EntityNotFound('Empresa não está cadastrada')

        return self.result_uuid(cliente)

    @http_response
    def save(self):
        arqs = parser.parse(CNPJ, request, location='view_args')
        cnpj = arqs['cnpj']

        company_controller = CompanyController()
        company = company_controller.find_and_save(cnpj)

        cliente = Cliente()
        cliente.uuid = uuid.uuid4().hex
        cliente.empresa_id = company.id

        # TODO - fazer requeste para outra API salvando os dados e retornando para edicao

        self.__repository.save(cliente)
        return self.result_uuid(cliente)

    def result_uuid(self, cliente: Cliente):
        return {'id': cliente.uuid}, 200
