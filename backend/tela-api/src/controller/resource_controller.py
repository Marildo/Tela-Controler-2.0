from telacore.models import Credential

from src.controller import BaseController
from src.controller.schemas import ResourceSchema
from src.model.entities import Recurso
from src.model.repository import RecursoRepository


class ResourceController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = ResourceSchema()
        self.ClassRepository = RecursoRepository
        self.ClassEntity = Recurso
