from abc import ABC
from typing import Dict, List, Union

from sqlalchemy import update, delete
from telacore.exceptions import DataBaseException

from model.config import DBConfig, Base
from model.config import DBConnection
from model.entities import BaseEntity
from telacore.utils.logger_util import log_error


class IRepository(ABC):

    def __init__(self, cnpj: str):
        config = DBConfig(cnpj)
        self.connection: DBConnection = DBConnection(config)
        Base.metadata.create_all(self.connection.get_engine())

    def find_all(self, entity: BaseEntity) -> List[BaseEntity]:
        with self.connection as conn:
            try:
                result = conn.session.query(entity).all()
                return result
            except Exception as e:
                log_error(e)
            finally:
                conn.session.close()

    def find_by_id(self, entity: BaseEntity, _id: int) -> Union[BaseEntity, None]:
        with self.connection as conn:
            try:
                result = conn.session.query(entity).filter(entity.id == _id).first()
                return result
            except Exception as e:
                log_error(e)
            finally:
                conn.session.close()

    def save(self, entity: BaseEntity)-> BaseEntity:
        with self.connection as conn:
            try:
                conn.session.add(entity)
                conn.session.commit()
                entity.id
                return entity
            except Exception as e:               
                conn.session.rollback()
                log_error(e)
                raise DataBaseException(e)
            finally:
                conn.session.close()

    def update(self, entity: BaseEntity, _id: int, data: Dict) -> BaseEntity:
        with self.connection as conn:
            try:
                if 'id' in data:
                    del data['id']
                conn.session.execute(
                    update(entity).where(entity.id == _id).values(data)
                )
                conn.session.commit()
                return self.find_by_id(entity,_id)
            except Exception as e:
                conn.session.rollback()
                log_error(e)
                raise DataBaseException(e)
            finally:
                conn.session.close()


    def delete(self, entity: BaseEntity, _id: int) -> int:
        with self.connection as conn:
            try:
                rs =  conn.session.execute(
                    delete(entity).where(entity.id == _id)
                )
                conn.session.commit()
                return rs.rowcount
            except Exception as e:
                conn.session.rollback()
                log_error(e)
                raise DataBaseException(e)
            finally:
                conn.session.close()