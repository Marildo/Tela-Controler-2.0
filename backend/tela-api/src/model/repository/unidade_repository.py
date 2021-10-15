from .base_repository import IRepository
from ..entities import Unidade


class UnidadeRepository(IRepository):

    def translate_field(self, fieldname: str):
        fields = {
            'unid': Unidade.unid,
            'descricao': Unidade.descricao,
        }
        return fields[fieldname] if fieldname in fields else None
