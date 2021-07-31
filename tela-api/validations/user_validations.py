from webargs import fields, validate

user_args = {
    "email": fields.Email(required=True),
    "password": fields.Str(required=True, validate=[validate.Length(min=6, max=30)])
}
