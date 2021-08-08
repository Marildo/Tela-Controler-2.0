import datetime

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

        return {'id': cliente.uuid}, 200

    @http_response
    def save(self):
        arqs = parser.parse(CNPJ, request, location='view_args')
        cnpj = arqs['cnpj']
        cnpj = CNPJUtil.mask(cnpj)

        cliente = self.__repository.find(cnpj)
        if cliente:
            cliente.last_token = datetime.datetime.now()
            self.__repository.save(cliente)
            return {'token': cliente.uuid}, 200

        company_controller = CompanyController()
        company = company_controller.find_and_save(cnpj)
        cliente = Cliente()
        cliente.uuid = CNPJUtil.encode(cnpj)
        cliente.empresa_id = company.id
        self.__repository.save(cliente)
        return {'token': cliente.uuid}, 201
