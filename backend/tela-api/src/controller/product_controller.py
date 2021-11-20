from typing import Dict, Tuple

from src.controller.schemas import ProductSchema
from src.model.entities import Produto, Unidade
from src.model.repository import ProdutoRepository,UnidadeRepository
from telacore.models import Credential
from .base_controller import BaseController


class ProductController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = ProductSchema()
        self.ClassRepository = ProdutoRepository
        self.ClassEntity = Produto

    def create_and_dump(self, data: Dict) -> Tuple[Dict, int]:
        unidade_id = data['unidade']['id']
        setor_id = data['setor']['id']

        del data['unidade']
        del data['setor']

        produto = Produto(**data)
        produto.unidade_id = unidade_id
        produto.setor_id = setor_id

        with self.repository as rep:
            rep.save(produto)
            data = self.schema.dump(produto)

            return data, 201
