from abc import ABC
from typing import Dict, List, Union

from sqlalchemy import update, delete
from sqlalchemy.exc import IntegrityError
from telacore.exceptions import DataBaseException, DuplicateErrorException
from telacore.utils.logger_util import log_error

from src.model.config import DBConfig
from src.model.connection import DBConnection
from src.model.entities import BaseEntity


class IRepository(ABC):

    def __init__(self, cnpj: str):
        self.cnpj = cnpj
        config = DBConfig(cnpj)
        self.connection: DBConnection = DBConnection(config)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def find_all(self, entity: BaseEntity) -> List[BaseEntity]:
        with self.connection as conn:
            try:
                result = conn.session.query(entity).all()
                return result
            except Exception as e:
                log_error(e)
                raise DataBaseException(e)

    def find_by_id(self, entity: BaseEntity, _id: int) -> Union[BaseEntity, None]:
        with self.connection as conn:
            try:
                result = conn.session.query(entity).filter(entity.id == _id).first()
                return result
            except Exception as e:
                log_error(e)
                raise DataBaseException(e)

    def save(self, entity: BaseEntity) -> BaseEntity:
        with self.connection as conn:
            try:
                conn.session.add(entity)
                conn.session.commit()
                return entity
            except IntegrityError as error:
                conn.session.rollback()
                log_error(error)
                raise DuplicateErrorException(error)
            except Exception as e:
                conn.session.rollback()
                log_error(e)
                raise DataBaseException(e)

    def update(self, entity: BaseEntity, _id: int, data: Dict) -> BaseEntity:
        with self.connection as conn:
            try:
                if 'id' in data:
                    del data['id']
                conn.session.execute(
                    update(entity).where(entity.id == _id).values(data)
                )
                conn.session.commit()
                return self.find_by_id(entity, _id)
            except Exception as e:
                conn.session.rollback()
                log_error(e)
                raise DataBaseException(e)

    def delete(self, entity: BaseEntity, _id: int) -> int:
        with self.connection as conn:
            try:
                rs = conn.session.execute(
                    delete(entity).where(entity.id == _id)
                )
                conn.session.commit()
                return rs.rowcount
            except Exception as e:
                conn.session.rollback()
                log_error(e)
                raise DataBaseException(e)
