from webargs import fields, validate

SECTION_ARGS = {
    'id': fields.Int(),
    'nome': fields.Str(required=True, validate=[validate.Length(min=1, max=30)]),
    'ativo': fields.Boolean()
}
