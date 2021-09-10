from telacore.models import Credential

from src.controller import BaseController
from src.controller.schemas import CustomerSchema
from src.model.entities import Participante
from src.model.repository import ParticipanteRepository


class CustomerController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = CustomerSchema()
        self.ClassRepository = ParticipanteRepository
        self.ClassEntity = Participante

