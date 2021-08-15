from abc import ABC, abstractmethod
from typing import Dict


class IAuth(ABC):

    @abstractmethod
    def encode(self, cnpj: str, payload: Dict) -> str:
        pass

    @abstractmethod
    def decode(self, token: str) -> str:
        pass
