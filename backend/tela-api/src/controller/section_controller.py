from telacore.models import Credential

from src.controller import BaseController
from src.controller.schemas import SectionSchema
from src.model.entities import Setor
from src.model.repository import SetorRepository


class SectionController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = SectionSchema()
        self.ClassRepository = SetorRepository
        self.ClassEntity = Setor

    def create(self, args):
        section = Setor(**args)
        return self.create_and_dump(section)

