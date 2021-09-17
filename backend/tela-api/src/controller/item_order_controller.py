from telacore.models import Credential

from src.controller import BaseController
from src.controller.schemas import ItemOrderSchema
from src.model.entities import ItensPedido
from src.model.repository import ItensPedidoRepository


class ItemOrderController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = ItemOrderSchema()
        self.ClassRepository = ItensPedidoRepository
        self.ClassEntity = ItensPedido

