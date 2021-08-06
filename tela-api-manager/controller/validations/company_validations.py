from brutils import cnpj
from webargs import fields, ValidationError


def valida_cnpj(value):
    if not cnpj.validate(str(value).rjust(14, '0')):
        raise ValidationError('CNPJ inválido')
    return True


BY_CNPJ = {
    'cnpj': fields.Int(required=True, validate=valida_cnpj),
}
