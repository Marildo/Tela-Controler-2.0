from typing import Dict, Tuple

from telacore.models import Credential

from src.controller.schemas import ProductSchema
from src.model.entities import Produto
from src.model.repository import ProdutoRepository
from .base_controller import BaseController


class ProductController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = ProductSchema()
        self.ClassRepository = ProdutoRepository
        self.ClassEntity = Produto

    # def create(self, args: Dict) -> Tuple:
    #     # product = Produto(**args)
    #     return self.create_and_dump(args)
