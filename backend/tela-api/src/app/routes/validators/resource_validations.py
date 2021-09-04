from webargs import fields, validate

CREATE_RESOURCE_ARGS = {'nome': fields.Str(required=True, validate=[validate.Length(min=5, max=60)])}
