from abc import ABC

from telacore.exceptions import DataBaseException

from model.config import DBConfig, Base
from model.config import DBConnection
from model.entities import BaseEntity


class IRepository(ABC):

    def __init__(self):
        config = DBConfig()
        self.connection: DBConnection = DBConnection(config)
        Base.metadata.create_all(self.connection.get_engine())

    def save(self, entity: BaseEntity):
        with self.connection as conn:
            try:
                conn.session.add(entity)
                conn.session.commit()
                return entity
            except Exception as e:
                conn.session.rollback()
                raise DataBaseException(e)
            finally:
                conn.session.close()
