import re
from abc import ABC
from base64 import b64encode

from brutils import cnpj


class IEncoderCNPJ(ABC):
    def encode(self, _cnpj: str):
        raise NotImplementedError


#TODO - Deve ser implementada pelo projeto que chamar a library
class Encoder(IEncoderCNPJ):
    def __init__(self, operation: str, value: str):
        self.operation = operation
        self.value = value

    def encode(self, _cnpj: str):
        return eval(f'{_cnpj}{self.operation}{self.value}')


class CNPJUtil:

    @staticmethod
    def validate(_cnpj) -> bool:
        return cnpj.validate(_cnpj)

    @staticmethod
    def mask(_cnpj) -> str:
        value = re.sub(r'\D', '', str(_cnpj))
        return cnpj.display(value)

    @staticmethod
    def encode(_cnpj, encoder: IEncoderCNPJ) -> str:
        encoding = 'utf-8'
        value = re.sub(r'\D', '', str(_cnpj))
        value = encoder.encode(value)
        value = str(value).encode(encoding)
        value = bytes(value)
        value = b64encode(value)
        return value.decode(encoding)
