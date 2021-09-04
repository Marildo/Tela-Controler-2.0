from typing import Dict, Tuple

from telacore.models import Credential
from telacore.utils import SecurityUtil

from src.controller import BaseController
from src.controller.schemas import UsuarioSchema
from src.model.entities import Usuario
from src.model.repository import UsuarioRepository


class UserController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = UsuarioSchema()
        self.ClassRepository = UsuarioRepository
        self.ClassEntity = Usuario

    def create(self, args: Dict):
        password = SecurityUtil.hash(args['password'])
        user = Usuario(email=args['email'], nome=args['nome'], password=password)
        data = self.__save_user(self.cnpj, user)
        return data, 201

    def __save_user(self, cnpj: str, user: Usuario) -> Dict:
        repository = UsuarioRepository(cnpj)
        repository.save(user)

        data = self.schema.dump(user)
        return data

    def read_by_id_and_dump(self, _id: int) -> Tuple[Dict, int]:
        with self.repository as rep:
            result = rep.find_by_id(self.ClassEntity, _id)
            data = self.schema.dump(result)
            permissions = rep.load_permissions(_id)
            data.update({'permissoes': permissions})
            return data, 200

    def update(self, _id: int, args: Dict):
        if 'password' in args:
            del args['password']
        return self.update_and_dump(_id, args)

    def change_password(self, _id: int, args: Dict):
        password = SecurityUtil.hash(args['password'])
        return self.update_and_dump(_id, {'password': password})
