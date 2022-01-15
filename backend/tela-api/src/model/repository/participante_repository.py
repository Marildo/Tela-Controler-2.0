from .base_repository import IRepository
from ..entities import Participante


class ParticipanteRepository(IRepository):

    def translate_field(self, fieldname: str):
        fields = {
            'nome': Participante.nome,
        }
        return fields[fieldname] if fieldname in fields else None

