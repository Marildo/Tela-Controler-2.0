from abc import ABC
from typing import Dict

from sqlalchemy import update
from telacore.exceptions import DataBaseException

from model.config import DBConfig, Base
from model.config import DBConnection
from model.entities import BaseEntity


class IRepository(ABC):

    def __init__(self, cnpj: str):
        config = DBConfig(cnpj)
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

    def update(self, entity: BaseEntity, _id: int, data: Dict) -> int:
        with self.connection as conn:
            try:
                conn.session.execute(
                    update(entity).where(entity.id == _id).values(data)
                )
                conn.session.commit()
                return _id
            except Exception as e:
                conn.session.rollback()
                raise DataBaseException(e)
            finally:
                conn.session.close()
