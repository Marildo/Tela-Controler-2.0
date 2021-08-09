from webargs import fields, ValidationError

from utils import CNPJUtil

def valida_cnpj(value):
    if not CNPJUtil.validate(str(value).rjust(14, '0')):
        raise ValidationError('CNPJ inválido')
    return True

CNPJ = {
    'cnpj': fields.Int(required=True, validate=valida_cnpj),
}
