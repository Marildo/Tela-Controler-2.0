import re
from abc import ABC
from base64 import b64encode, b64decode

from brutils import cnpj as cnpj_lib
from webargs import ValidationError


class IEncoderCNPJ(ABC):
    def encode(self, cnpj: str) -> str:
        raise NotImplementedError

    def decode(self, cnpj: str) -> str:
        raise NotImplementedError


# TODO - Deve ser implementada pelo projeto que chamar a library
class Encoder(IEncoderCNPJ):
    def __init__(self):
        self.encoding = 'utf-8'

    def encode(self, cnpj: str) -> str:
        value = int(cnpj) * 33
        return value

    def decode(self, cnpj: str) -> str:
        value = int(int(cnpj) / 33)
        value = str(value).rjust(14, '0')
        return value


class CNPJUtil:

    @staticmethod
    def validate(cnpj: str, raise_exception: bool = True) -> bool:
        value = CNPJUtil.unmask(cnpj)
        result = cnpj_lib.validate(value)
        if raise_exception and not result:
            raise ValidationError('CNPJ Inválido')
        return result

    @staticmethod
    def mask(cnpj) -> str:
        value = CNPJUtil.unmask(cnpj)
        value = cnpj_lib.display(str(value))
        return value

    @staticmethod
    def unmask(cnpj: str) -> int:
        value = int(re.sub(r'\D', '', str(cnpj)))
        value = str(value).rjust(14, '0')
        return value

    @staticmethod
    def encode(cnpj) -> str:
        encoder = Encoder()

        value = CNPJUtil.unmask(cnpj)
        value = encoder.encode(value)
        value = str(value).encode(encoder.encoding)
        value = bytes(value)
        value = b64encode(value)
        return value.decode(encoder.encoding)

    @staticmethod
    def decode(_encodec) -> str:
        try:
            encoder = Encoder()
            value = b64decode(_encodec)
            decoded = encoder.decode(value)
            assert CNPJUtil.validate(decoded), ''
        except Exception as err:
            raise Exception('Código Inválido')

        return decoded
