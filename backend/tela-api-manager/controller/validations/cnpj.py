from telacore.utils import cnpj_util
from webargs import fields, ValidationError


def valida_cnpj(value):
    if not cnpj_util.validate(str(value).rjust(14, '0')):
        raise ValidationError('CNPJ inválido')
    return True


CNPJ = {
    'cnpj': fields.Int(required=True, validate=valida_cnpj),
}
