from telacore.utils import CNPJUtil
from webargs import fields, validate

SAVE_COMPANY = {
    'cnpj': fields.Int(required=True, validate=CNPJUtil.validate),
    'email': fields.Email(required=True),
    'contato': fields.Str(required=True, validate=validate.Length(min=2))
}

CNPJ = {
    'cnpj': fields.Int(required=True, validate=CNPJUtil.validate)
}
