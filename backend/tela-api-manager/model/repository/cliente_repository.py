from model.entities.cliente import Cliente
from model.entities.empresa import Empresa
from .base_repository import IRepository


class ClienteRepository(IRepository):

    def find(self, cnpj: str) -> Cliente:
        with self.connection as conn:
            try:
                client = conn.session.query(Cliente) \
                    .join(Empresa, Empresa.id == Cliente.empresa_id) \
                    .filter(Empresa.cnpj == cnpj).first()
                if client:
                    client.contatos
                return client
            finally:
                conn.session.close()
