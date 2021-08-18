from webargs import fields, validate


def notExists(unit: str):
    print(unit)
    return True


CREATE_UNITY_ARG = {
    'unid': fields.Str(required=True, validate=[validate.Length(min=1, max=6), notExists]),
    'descricao': fields.Str(validate=[validate.Length(min=1, max=30)]),
    'fracionavel': fields.Boolean()
}
