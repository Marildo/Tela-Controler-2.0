from telacore.utils import cnpj_util
from webargs import fields, ValidationError, validate


def valida_cnpj(value):
    if not cnpj_util.validate(str(value).rjust(14, '0')):
        raise ValidationError('CNPJ inválido')
    return True


SAVE_COMPANY = {
    'cnpj': fields.Int(required=True, validate=valida_cnpj),
    'email': fields.Email(required=True),
    'contato': fields.Str(required=True, validate=validate.Length(min=2))
}

CNPJ = {
    'cnpj': fields.Int(required=True, validate=valida_cnpj)
}
