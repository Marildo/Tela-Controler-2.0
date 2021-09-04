from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from telacore.exceptions import DataBaseException, DuplicateErrorException
from telacore.utils.logger_util import log_error

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

    def save(self, user: Usuario) -> Usuario:
        with self.connection as conn:
            try:
                conn.session.add(user)
                conn.session.commit()
                self.__set_permissoes(user.id, True)
                return user
            except IntegrityError as error:
                conn.session.rollback()
                log_error(error)
                raise DuplicateErrorException(error)
            except Exception as e:
                conn.session.rollback()
                log_error(e)
                raise DataBaseException(e)

    def __set_permissoes(self, usuario_id: int, permissao: bool):
        sql = text(
            'INSERT INTO permissoes(recurso_id, usuario_id, c, r, u, d) ' +
            'SELECT id,:user, :c, :r, :u, :d FROM recursos;'
        )
        params = {
            'user': usuario_id,
            'c': permissao,
            'r': permissao,
            'u': permissao,
            'd': permissao
        }

        with self.connection.engine.begin() as conn:
            conn.execute(sql, params)
