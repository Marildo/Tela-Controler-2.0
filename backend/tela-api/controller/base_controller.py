from abc import ABC

from telacore.models import Credential


class BaseController(ABC):

    def __init__(self):
        self.credential: Credential = None

    @property
    def cnpj(self) -> str:
        return self.credential.cnpj
