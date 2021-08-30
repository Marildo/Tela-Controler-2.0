from src.model.entities import Empresa
from .base_repository import IRepository


class EmpresaRepository(IRepository):

    def find(self, ) -> Empresa:
        with self.connection as conn:
            try:
                result = conn.session.query(Empresa).first()
                return result
            finally:
                conn.session.close()
