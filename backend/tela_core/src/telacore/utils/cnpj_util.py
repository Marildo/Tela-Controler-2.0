import re
from abc import ABC
from base64 import b64encode, b64decode

from brutils import cnpj


class IEncoderCNPJ(ABC):
    def encode(self, _cnpj: str) -> str:
        raise NotImplementedError

    def decode(self, _cnpj: str) -> str:
        raise NotImplementedError


# TODO - Deve ser implementada pelo projeto que chamar a library
class Encoder(IEncoderCNPJ):
    def __init__(self):
        self.encoding = 'utf-8'

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
    value = cnpj.display(str(value))
    return value


def unmask(_cnpj: str) -> int:
    value = int(re.sub(r'\D', '', str(_cnpj)))
    value = str(value).rjust(14, '0')
    return value


def encode(_cnpj) -> str:
    encoder = Encoder()

    value = unmask(_cnpj)
    value = encoder.encode(value)
    value = str(value).encode(encoder.encoding)
    value = bytes(value)
    value = b64encode(value)
    return value.decode(encoder.encoding)


def decode(_encodec) -> str:
    encoder = Encoder()
    value = b64decode(_encodec)
    decoded = encoder.decode(value)
    assert validate(decoded), 'Código Inválido'
    return decoded
