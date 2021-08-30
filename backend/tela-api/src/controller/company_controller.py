from typing import Dict

from telacore.exceptions import EntityNotFound
from telacore.models import Credential
from telacore.utils import CNPJUtil

from src.controller import BaseController
from src.controller import auth_controller
from src.controller.schemas import EmpresaSchema
from src.model.entities import Empresa
from src.model.repository import EmpresaRepository
from src.services import Manager


class CompanyController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = EmpresaSchema()
        self.ClassRepository = EmpresaRepository
        self.ClassEntity = Empresa

    def create(self, args: Dict):
        cnpj = CNPJUtil.decode(args['codigo'])
        data = Manager.find_company(cnpj)
        if not data:
            raise EntityNotFound('Empresa não localizada')

        token = auth_controller.create_user_and_login(cnpj, args)

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
