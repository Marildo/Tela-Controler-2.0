from typing import Dict, Tuple

from src.controller.schemas import ProductSchema
from src.model.entities import Produto
from src.model.repository import ProdutoRepository
from telacore.models import Credential
from .base_controller import BaseController


class ProductController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = ProductSchema()
        self.classRepository = ProdutoRepository
        self.classEntity = Produto

    def create_and_dump(self, data: Dict) -> Tuple[Dict, int]:
        data = self.__prepare_product(data)
        produto = Produto(**data)
        with self.repository as rep:
            rep.save(produto)
            produto = rep.find_by_field(Produto, 'codigo', produto.codigo)
            data = self.schema.dump(produto)
            return data, 201

    def update_and_dump(self, _id: int, args) -> Tuple[Dict, int]:
        data = self.__prepare_product(args)
        return super().update_and_dump(_id, data)

    def __prepare_product(self, data: Dict) -> Dict:
        data['unidade_id'] = data['unidade']['id']
        data['setor_id'] = data['setor']['id']
        del data['unidade']
        del data['setor']
        return data
