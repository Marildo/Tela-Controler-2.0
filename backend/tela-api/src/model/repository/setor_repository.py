from .base_repository import IRepository
from src.model.entities import Setor

class SetorRepository(IRepository):

    def translate_field(self, fieldname: str):
        fields = {
            'name': Setor.nome,
        }
        return fields[fieldname] if fieldname in fields else None

