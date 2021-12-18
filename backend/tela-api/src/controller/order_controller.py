from telacore.models import Credential

from src.controller import BaseController
from src.controller.schemas import OrderSchema
from src.model.entities import Pedido
from src.model.repository import PedidoRepository


class OrderController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = OrderSchema()
        self.classRepository = PedidoRepository
        self.classEntity = Pedido

