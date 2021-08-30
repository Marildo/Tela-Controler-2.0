from abc import ABC, abstractmethod
from typing import Dict, Tuple

from marshmallow_sqlalchemy import SQLAlchemySchema
from telacore.models import Credential

from src.model.entities import BaseEntity
from src.model.repository import IRepository


class BaseController(ABC):

    def __init__(self):
        self.ClassRepository: IRepository = None
        self.schema: SQLAlchemySchema = None
        self.ClassEntity: BaseEntity = None
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
        return self.ClassRepository(self.cnpj)

    def read_all_and_dump(self) -> Tuple[Dict, int]:
        result = self.repository.find_all(self.ClassEntity)
        data = self.schema.dump(result, many=True)

        return data, 200

    def read_by_id_and_dump(self, _id: int) -> Tuple[Dict, int]:
        result = self.repository.find_by_id(self.ClassEntity, _id)
        data = self.schema.dump(result)

        return data, 200

    def create_and_dump(self, entity: BaseEntity) -> Tuple[Dict, int]:
        self.repository.save(entity)
        data = self.schema.dump(entity)

        return data, 201

    def update_and_dump(self, _id: int, args) -> Tuple[Dict, int]:
        entity = self.repository.update(self.ClassEntity, _id, args)
        data = self.schema.dump(entity)

        return data, 200

    def delete_and_dump(self, _id: int) -> Tuple[Dict, int]:
        rows = self.repository.delete(self.ClassEntity, _id)
        data = {'rows_affected': rows}

        return data, 200
