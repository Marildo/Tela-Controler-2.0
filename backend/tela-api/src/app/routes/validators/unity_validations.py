from webargs import fields, validate

id = {'id': fields.Int()}
unid = {'unid': fields.Str(required=True, validate=[validate.Length(min=2, max=4)])}
descricao = {'descricao': fields.Str(validate=[validate.Length(min=1, max=30)])}
fracionavel = {'fracionavel': fields.Boolean()}
ativo = {'ativo': fields.Boolean()}


CREATE_UNITY_ARGS = {}
CREATE_UNITY_ARGS.update(id)
CREATE_UNITY_ARGS.update(unid)
CREATE_UNITY_ARGS.update(fracionavel)
CREATE_UNITY_ARGS.update(descricao)
CREATE_UNITY_ARGS.update(ativo)

UPDATE_UNITY_ARGS = CREATE_UNITY_ARGS.copy()




