import re
from base64 import b64encode

from brutils import cnpj


class CNPJUtil:

    @staticmethod
    def validate(_cnpj) -> bool:
        return cnpj.validate(_cnpj)

    @staticmethod
    def mask(_cnpj) -> str:
        value = re.sub(r'\D', '', str(_cnpj))
        return cnpj.display(value)

    @staticmethod
    def encode(_cnpj) -> str:
        encoding = 'utf-8'
        value = re.sub(r'\D', '', str(_cnpj))
        value = int(value) * 33
        value = str(value).encode(encoding)
        value = bytes(value)
        value = b64encode(value)
        return value.decode(encoding)
