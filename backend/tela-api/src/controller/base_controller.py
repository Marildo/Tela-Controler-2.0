from abc import ABC, abstractmethod
from typing import Dict, Tuple

from marshmallow_sqlalchemy import SQLAlchemySchema
from telacore.models import Credential, QueryPage, Pagination

from src.model.entities import BaseEntity
from src.model.repository import IRepository


class BaseController(ABC):

    def __init__(self):
        self.classRepository: IRepository = None
        self.schema: SQLAlchemySchema = None
        self.classEntity: BaseEntity = None
        self.credential: Credential = None

    @abstractmethod
    def initialize(self, credential: Credential):
        self.credential: Credential = credential
        raise NotImplementedError('Must be implemented in child classes')

    @property
    def cnpj(self) -> str:
        return self.credential.cnpj

    @property
    def repository(self):
        repository = self.classRepository(self.cnpj)
        return repository

    def read_all_and_dump(self, query: QueryPage) -> Tuple[Dict, int, Pagination]:
        with self.repository as rep:
            data, pagination = rep.find_all(self.classEntity, query)
            data = self.schema.dump(data, many=True)

            return data, 200, pagination

    def read_by_id_and_dump(self, _id: int) -> Tuple[Dict, int]:
        with self.repository as rep:
            result = rep.find_by_id(self.classEntity, _id)
            data = self.schema.dump(result)

            return data, 200

    def create_and_dump(self, data: Dict) -> Tuple[Dict, int]:
        if 'id' in data:
            data['id'] = None

        with self.repository as rep:
            entity = self.classEntity(**data)
            rep.save(entity)
            data = self.schema.dump(entity)

            return data, 201

    def update_and_dump(self, _id: int, args) -> Tuple[Dict, int]:
        with self.repository as rep:
            entity = rep.update(self.classEntity, _id, args)
            data = self.schema.dump(entity)
            return data, 200

    def delete_and_dump(self, _id: int) -> Tuple[Dict, int]:
        with self.repository as rep:
            rows = rep.delete(self.classEntity, _id)
            data = {'rows_affected': rows}

            return data, 200

    def soft_delete_and_dump(self, _id: int) -> Tuple[Dict, int]:
        with self.repository as rep:
            rep.update(self.classEntity, _id, {'ativo': False})
            data = {'rows_affected': 1}

            return data, 200
