from telacore.models import Credential

from src.controller import BaseController
from src.controller.schemas import ItemOrderSchema
from src.model.entities import Pedido
from src.model.repository import PedidoRepository


class ItemOrderController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = ItemOrderSchema()
        self.ClassRepository = PedidoRepository
        self.ClassEntity = Pedido

