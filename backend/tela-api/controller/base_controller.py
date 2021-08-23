from abc import ABC, abstractmethod

from marshmallow_sqlalchemy import SQLAlchemySchema
from telacore.models import Credential

from model.entities import BaseEntity
from model.repository import IRepository


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

    def create_and_dump(self, entity: BaseEntity):
        self.repository.save(entity)
        data = self.schema.dump(entity)

        return data, 201

    def read_all_and_dump(self):
        result = self.repository.find_all(self.ClassEntity)
        data = self.schema.dump(result, many=True)

        return data, 200
