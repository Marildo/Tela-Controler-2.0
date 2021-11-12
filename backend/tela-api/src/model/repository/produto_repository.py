from .base_repository import IRepository
from ..entities import Produto


class ProdutoRepository(IRepository):

    def translate_field(self, fieldname: str):
        fields = {
            'name': Produto.nome,
            'codigo': Produto.codigo,
            'codigo_barras': Produto.cod_barras
        }
        return fields[fieldname] if fieldname in fields else None
