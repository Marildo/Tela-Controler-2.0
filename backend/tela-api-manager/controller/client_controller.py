import datetime

from flask import request
from telacore.decorators import http_response
from telacore.exceptions import EntityNotFound
from telacore.utils import cnpj_util
from webargs.flaskparser import parser

from controller import CompanyController
from controller.validations import SAVE_COMPANY, CNPJ
from model.entities import Cliente, Contato
from model.repository import ClienteRepository


class ClientController:

    def __init__(self):
        self.__repository = ClienteRepository()

    @http_response
    def load(self):
        arqs = parser.parse(CNPJ, request, location='json')
        cnpj = cnpj_util.mask(arqs['cnpj'])

        cliente = self.__find_client(cnpj)
        if not cliente:
            raise EntityNotFound('Empresa não está cadastrada')

        return {'codigo': cliente.uuid}, 200

    @http_response
    def save(self):
        arqs = parser.parse(SAVE_COMPANY, request, location='json')
        cnpj = arqs['cnpj']
        cnpj = cnpj_util.mask(cnpj)

        cliente = self.__find_client(cnpj)
        if not cliente:
            company_controller = CompanyController()
            company = company_controller.find_and_save(cnpj)
            cliente = Cliente()
            cliente.uuid = cnpj_util.encode(cnpj)
            cliente.empresa_id = company.id
            self.__repository.save(cliente)

            email = arqs['email']
            nome = arqs['contato']
            contato = Contato(email=email, nome=nome, client_id=cliente.id)
            self.__repository.save(contato)
            cliente.contatos = [contato]

        return {
                   'codigo': cliente.uuid,
                   'email': cliente.contatos[0].email
               }, 201

    def __find_client(self, cnpj) -> Cliente:
        cliente = self.__repository.find(cnpj)
        if cliente:
            cliente.last_token = datetime.datetime.now()
            self.__repository.save(cliente)
            return cliente

        return None
