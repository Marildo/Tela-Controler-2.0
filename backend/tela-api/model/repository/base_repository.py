from abc import ABC

from model.config import DBConfig, Base
from model.config import DBConnection
from model.entities import BaseEntity
from telacore.exceptions import DataBaseException


class IRepository(ABC):

    def __init__(self, config: DBConfig):
        self.connection: DBConnection = DBConnection(config)

    def save(self, entity: BaseEntity):
        with self.connection as conn:
            try:
                Base.metadata.create_all(conn.get_engine())
                conn.session.expire_on_commit = False
                conn.session.add(entity)
                conn.session.commit()
                return entity
            except Exception as e:
                conn.session.rollback()
                raise DataBaseException(e)
            finally:
                conn.session.close()
