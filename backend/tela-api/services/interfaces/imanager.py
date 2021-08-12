from abc import ABC, abstractmethod
from typing import Dict


class IManager(ABC):

    @abstractmethod
    def find_company(self, _cnpj: str) -> Dict:
        raise NotImplementedError
