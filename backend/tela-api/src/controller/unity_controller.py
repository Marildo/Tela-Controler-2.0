from telacore.models import Credential

from src.controller import BaseController
from src.controller.schemas import UnitySchema
from src.model.entities import Unidade
from src.model.repository import UnidadeRepository
from typing import Dict,List,Tuple

#TODO - Mudar em produto de UN para Id

class UnityController(BaseController):

    def initialize(self, credential: Credential):
        self.credential = credential
        self.schema = UnitySchema()
        self.ClassRepository = UnidadeRepository
        self.ClassEntity = Unidade


    def create_and_dump(self, data: Dict) -> Tuple[Dict, int]:
        entity = self.ClassEntity(**data)

        with self.repository as rep:
            print(data)

            rep.save(entity)
            data = self.schema.dump(entity)

            return data, 201