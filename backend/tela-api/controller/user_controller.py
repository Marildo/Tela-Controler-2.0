from typing import Dict

from telacore.models import Credential
from telacore.utils import SecurityUtil

from controller import BaseController
from controller.schemas import UsuarioSchema
from model.entities import Usuario
from model.repository import UsuarioRepository
from services import AuthService


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

    def create_user_and_login(self, cnpj, args) -> str:
        email = args['email']
        nome = args['nome']
        password = SecurityUtil.hash(args['password'])

        user = Usuario(email=email, nome=nome, password=password)
        data = self.__save_user(cnpj, user)
        token = AuthService().encode(cnpj, data)
        return token

    def __save_user(self, cnpj: str, user: Usuario) -> Dict:
        repository = UsuarioRepository(cnpj)
        repository.save(user)
        data = self.schema.dump(user)
        return data
