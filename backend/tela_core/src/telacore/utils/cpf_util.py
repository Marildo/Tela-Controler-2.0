import re

from brutils import cpf as cpf_lib
from webargs import ValidationError


class CPFUtil:

    @staticmethod
    def validate(cnpj: str, raise_exception: bool = True) -> bool:
        value = CPFUtil.unmask(cnpj)
        result = cpf_lib.validate(value)
        if raise_exception and not result:
            raise ValidationError('CPF Inválido')
        return result

    @staticmethod
    def mask(cnpj) -> str:
        value = CPFUtil.unmask(cnpj)
        value = cpf_lib.display(str(value))
        return value

    @staticmethod
    def unmask(cnpj: str) -> str:
        value = re.sub(r'\D', '', str(cnpj))
        value = str(value).rjust(11, '0')
        return value

    @staticmethod
    def generate() -> str:
        return CPFUtil.mask(cpf_lib.generate())