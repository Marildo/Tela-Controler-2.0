from webargs import fields, validate

UNITY_ARGS = {
    'id': fields.Int(),
    'unid': fields.Str(required=True, validate=[validate.Length(min=2, max=4)]),
    'descricao': fields.Str(validate=[validate.Length(min=1, max=30)]),
    'fracionavel': fields.Boolean(),
    'ativo': fields.Boolean()
}
