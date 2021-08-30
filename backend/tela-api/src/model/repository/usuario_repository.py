from src.model.entities import Usuario
from .base_repository import IRepository


class UsuarioRepository(IRepository):

    def find_by_email(self, email) -> Usuario:
        with self.connection as conn:
            try:
                return conn.session.query(Usuario). \
                    filter(Usuario.email == email).first()
            finally:
                conn.session.close()
