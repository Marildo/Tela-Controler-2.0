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

    def create(self, args):
        unity = Unidade(**args)
        return self.create_and_dump(unity)

    def read_all(self):
        return self.read_all_and_dump()

    def read_by_id(self, _id: int):
        # TODO - Read unidade by id
        return {'msg:': f'Read By Id {_id}'}, 200

    def update(self, _id: int):
        # TODO - Update unidade
        return {'msg:': f'update {_id}'}, 200

    def delete(self, _id: int):
        # TODO - Delete unidade
        return {'msg:': f'delete {_id}'}, 200
