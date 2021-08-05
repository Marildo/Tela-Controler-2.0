from model.entities import Empresa
from .base_repository import IRepository


class EmpresaRepository(IRepository):

    def find_by_cnpj(self, cnpj) -> Empresa:
        with self.connection as conn:

            try:
                return conn.session.query(Empresa). \
                    filter(Empresa.cnpj == cnpj).first()
            finally:
                conn.session.close()
