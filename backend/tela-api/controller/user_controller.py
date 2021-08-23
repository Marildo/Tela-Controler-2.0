from typing import Dict

from telacore.models import Credential

from controller import BaseController
from controller.schemas import UsuarioSchema
from model.entities import Usuario
from model.repository import UsuarioRepository


class UserController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = UsuarioSchema()
        self.ClassRepository = UsuarioRepository
        self.ClassEntity = Usuario

    def create(self, args: Dict):
        user = Usuario(email=args['email'], nome=args['nome'], password=args['password'])
        data = self.__save_user(self.cnpj, user)
        return data, 201

    def __save_user(self, cnpj: str, user: Usuario) -> Dict:
        repository = UsuarioRepository(cnpj)
        repository.save(user)
        data = self.schema.dump(user)
        return data
