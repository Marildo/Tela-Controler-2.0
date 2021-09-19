from telacore.models import Credential

from src.controller import BaseController
from src.controller.schemas import UnitySchema
from src.model.entities import Unidade
from src.model.repository import UnidadeRepository

#TODO - Mudar em produto de UN para Id

class UnityController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = UnitySchema()
        self.ClassRepository = UnidadeRepository
        self.ClassEntity = Unidade

