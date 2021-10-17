from abc import ABC, abstractmethod
from typing import Dict, List, Union, Tuple

import sqlalchemy
from sqlalchemy import update, delete, and_
from sqlalchemy.exc import IntegrityError
from telacore.exceptions import DataBaseException, DuplicateErrorException
from telacore.models import QueryPage, Pagination
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

    @abstractmethod
    def translate_field(self, fieldname: str):
        raise NotImplementedError()

    def find_all(self, entity: BaseEntity, query_page: QueryPage) -> Tuple[List[BaseEntity], Pagination]:
        with self.connection as conn:
            try:
                # TODO - Tratar erro de ordenacao com campo inexistente

                filters = []
                field = self.translate_field(query_page.field_name)

                if field:
                    if query_page.field_like():
                        filters.append(field.ilike(f'%{query_page.field_value}%'))

                base_query = (conn.session
                              .query(entity)
                              .filter(and_(*filters)))

                total = base_query.count()

                sort = self.order_field(query_page)

                query = (base_query
                         .order_by(sort)
                         .limit(query_page.size)
                         .offset(query_page.offset)
                         )
                data = query.all()
                result = data, Pagination(total=total, page=query_page.page, size=query_page.size)
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

    def order_field(self, query_page: QueryPage):
        sort_function = {
            'desc': sqlalchemy.desc,
            'asc': sqlalchemy.asc
        }
        orderby, sort = query_page.orderby()
        if orderby:
            return sort_function[sort](orderby)
        return None
