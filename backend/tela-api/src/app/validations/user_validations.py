from webargs import fields, validate

validate_password = validate.Length(min=4, max=120)
validate_nome = validate.Length(min=4, max=120)

email = {'email': fields.Email(required=True)}
password = {'password': fields.Str(required=True, validate=validate_password)}

LOGIN_ARGS = {'codigo': fields.Str(required=True)}
LOGIN_ARGS.update(email)
LOGIN_ARGS.update(password)

CREATE_USER_ARGS = {
    'nome': fields.Str(required=True, validate=validate_nome)
}
CREATE_USER_ARGS.update(email)
CREATE_USER_ARGS.update(password)

UPDATE_USER_ARGS = {
    'email': fields.Email(),
    'password': fields.Str(validate=validate_password),
    'nome': fields.Str(validate=validate_nome)
}

CHANGE_PASSWORD_USER_ARGS = dict(password)