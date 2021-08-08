from model.entities import Empresa
from .base_repository import IRepository


class EmpresaRepository(IRepository):

    def find_by_cnpj(self, cnpj: str) -> Empresa:
        with self.connection as conn:
            try:
                result = conn.session.query(Empresa). \
                    filter(Empresa.cnpj == cnpj).first()
                return result
            finally:
                conn.session.close()
