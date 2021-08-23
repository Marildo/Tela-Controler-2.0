from typing import Dict

from flask import request
from telacore.exceptions import EntityNotFound
from telacore.models import Credential
from telacore.utils import CNPJUtil
from webargs.flaskparser import parser

from controller import BaseController, UserController
from controller.schemas import EmpresaSchema
from controller.validations.company_validations import UPDATE_COMPANY_ARGS
from model.entities import Empresa
from model.repository import EmpresaRepository
from services import Manager


class CompanyController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = EmpresaSchema()

    def create(self, args: Dict):
        cnpj = CNPJUtil.decode(args['codigo'])
        data = Manager.find_company(cnpj)
        if not data:
            raise EntityNotFound('Empresa não localizada')

        token = UserController().create_user_and_login(cnpj, args)

        empresa = Empresa()
        empresa.nome = data['razao_social']
        empresa.fantasia = data['nome_fantasia']
        empresa.cnpj = data['cnpj']
        empresa.cnae = data['cnae']
        empresa.ibge = data['ibge']
        empresa.uf = data['uf']
        empresa.cep = data['cep']
        empresa.logradouro = data['logradouro']
        empresa.numero = data['numero']
        empresa.complemento = data['complemento']
        empresa.bairro = data['bairro']
        empresa.fone = data['telefone']
        empresa.email = data['email']

        repository = EmpresaRepository(cnpj)
        repository.save(empresa)

        company = self.schema.dump(empresa)

        data = {
            'token': token,
            'company': company
        }

        return data, 201

    def read(self):
        repository = EmpresaRepository(self.cnpj)
        data = repository.find()
        data = self.schema.dump(data)
        return data, 200

    def update(self, _id):
        args = parser.parse(UPDATE_COMPANY_ARGS, request, location='json')
        del args['id']
        repository = EmpresaRepository(self.cnpj)
        repository.update(Empresa, _id, args)
        return {'id': _id}, 200
