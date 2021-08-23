from typing import Dict, Tuple

from telacore.models import Credential

from controller.schemas import ProductSchema
from model.entities import Produto
from model.repository import ProdutoRepository
from .base_controller import BaseController


class ProductController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = ProductSchema()
        self.ClassRepository = ProdutoRepository
        self.ClassEntity = Produto

    def create(self, args: Dict) -> Tuple:
        product = Produto(**args)
        return self.create_and_dump(product)
