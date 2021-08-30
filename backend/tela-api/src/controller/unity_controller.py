from telacore.models import Credential

from src.controller import BaseController
from src.controller.schemas import UnitySchema
from src.model.entities import Unidade
from src.model.repository import UnidadeRepository


class UnityController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = UnitySchema()
        self.ClassRepository = UnidadeRepository
        self.ClassEntity = Unidade

    def create(self, args):
        unity = Unidade(**args)
        return self.create_and_dump(unity)

