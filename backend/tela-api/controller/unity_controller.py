from telacore.models import Credential

from controller import BaseController
from controller.schemas import UnitySchema
from model.entities import Unidade
from model.repository import UnidadeRepository


class UnityController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = UnitySchema()
        self.ClassRepository = UnidadeRepository
        self.ClassEntity = Unidade

    def read_all(self):
        return self.read_all_and_dump()

    def read_by_id(self, _id: int):
        return self.read_by_id_and_dump(_id)

    def create(self, args):
        unity = Unidade(**args)
        return self.create_and_dump(unity)

    def update(self, args, _id: int):
        return self.update_and_dump(_id, args)

    def delete(self, _id: int):
        return self.delete_and_dump(_id)
