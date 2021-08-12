from webargs import fields, validate

CREATE_COMPANY_ARGS = {
       'email': fields.Email(required=True),
       'password': fields.Str(required=True, validate=[validate.Length(min=6, max=30)]),
       'nome': fields.Str(required=True, validate=[validate.Length(min=3, max=120)]),
       'codigo': fields.Str(required=True)
}