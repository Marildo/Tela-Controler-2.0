from webargs import fields, validate



ativo = {'ativo': fields.Boolean()}
fracionavel = {'ativo': fields.Boolean()}

CREATE_UNITY_ARG = {
    'unid': fields.Str(required=True, validate=[validate.Length(min=1, max=6)]),
    'descricao': fields.Str(validate=[validate.Length(min=1, max=30)]),
    'fracionavel': fields.Boolean(),
}

CREATE_UNITY_ARG.update(fracionavel)
