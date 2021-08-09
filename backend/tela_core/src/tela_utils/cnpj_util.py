import re
from abc import ABC
from base64 import b64encode

from brutils import cnpj


class IEncoderCNPJ(ABC):
    def encode(self, _cnpj: str) -> str:
        raise NotImplementedError

    def decode(self, _cnpj: str) -> str:
        raise NotImplementedError


# TODO - Deve ser implementada pelo projeto que chamar a library
class Encoder(IEncoderCNPJ):
    def encode(self, _cnpj: str) -> str:
        value = int(_cnpj) * 33
        return value

    def decode(self, _cnpj: str) -> str:
        value = int(int(_cnpj) / 33)
        value = str(value).rjust(14, '0')
        return value


def validate(_cnpj) -> bool:
    return cnpj.validate(_cnpj)


def mask(_cnpj) -> str:
    value = unmask(_cnpj)
    return cnpj.display(str(value))


def unmask(_cnpj: str) -> int:
    int(re.sub(r'\D', '', str(_cnpj)))


def encode(_cnpj, encoder: IEncoderCNPJ) -> str:
    encoding = 'utf-8'
    value = unmask(_cnpj)
    value = encoder.encode(value)
    value = str(value).encode(encoding)
    value = bytes(value)
    value = b64encode(value)
    return value.decode(encoding)
