from webargs import fields, validate

LOGIN_ARGS = {
    'email': fields.Email(required=True),
    'password': fields.Str(required=True, validate=[validate.Length(min=6, max=30)])
}

ADD_USER_ARGS = {
    'email': fields.Email(required=True),
    'password': fields.Str(required=True, validate=[validate.Length(min=6, max=30)]),
    'nome': fields.Str(required=True, validate=validate.Length(min=4, max=120))
}
