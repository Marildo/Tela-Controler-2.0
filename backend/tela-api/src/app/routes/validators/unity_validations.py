from webargs import fields, validate

unid = {'unid': fields.Str(required=True, validate=[validate.Length(min=1, max=4)])}
descricao = {'descricao': fields.Str(validate=[validate.Length(min=1, max=30)])}
fracionavel = {'fracionavel': fields.Boolean()}
ativo = {'ativo': fields.Boolean()}

CREATE_UNITY_ARGS = {}
CREATE_UNITY_ARGS.update(unid)
CREATE_UNITY_ARGS.update(fracionavel)
CREATE_UNITY_ARGS.update(descricao)

UPDATE_UNITY_ARGS = {
    'id': fields.Int()
}
UPDATE_UNITY_ARGS.update(unid)
UPDATE_UNITY_ARGS.update(fracionavel)
UPDATE_UNITY_ARGS.update(descricao)
UPDATE_UNITY_ARGS.update(ativo)


