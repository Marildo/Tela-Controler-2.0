from telacore.models import Credential

from src.controller import BaseController
from src.controller.schemas import AddressSchema
from src.model.entities import Endereco
from src.model.repository import EnderecoRepository


class AddressController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = AddressSchema()
        self.classRepository = EnderecoRepository
        self.classEntity = Endereco

