from webargs import fields, validate

id = {'id': fields.Int()}
codigo = {'codigo': fields.Str(required=True, validate=[validate.Length(min=1, max=30)])}
nome = {'nome': fields.Str(required=True, validate=[validate.Length(min=5, max=250)])}

PRODUCT_ARGS = dict()
PRODUCT_ARGS.update(id)
PRODUCT_ARGS.update(codigo)
PRODUCT_ARGS.update(nome)
