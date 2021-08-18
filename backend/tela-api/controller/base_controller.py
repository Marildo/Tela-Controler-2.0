from abc import ABC

from telacore.models import Credential

from model.entities import BaseEntity


class BaseController(ABC):

    def __init__(self):
        self.credential: Credential = None
        self.schema = None
        self.ClassEntity = None
        self.ClassRepository = None

    @property
    def cnpj(self) -> str:
        return self.credential.cnpj

    def create_and_dump(self, entity: BaseEntity):
        repository = self.ClassRepository(self.cnpj)
        repository.save(entity)
        data = self.schema.dump(entity)

        return data, 201

    def read_all_and_dump(self):
        repository = self.ClassRepository(self.cnpj)
        result = repository.find_all(self.ClassEntity)
        data = self.schema.dump(result, many=True)

        return data, 200
