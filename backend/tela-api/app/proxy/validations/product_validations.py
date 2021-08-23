from webargs import fields, validate

codigo = {'codigo': fields.Str(required=True, validate=[validate.Length(min=5, max=60)])}
descricao = {'descricao': fields.Str(required=True, validate=[validate.Length(min=5, max=250)])}

PRODUCT_CREATE_ARGS = dict()
PRODUCT_CREATE_ARGS.update(codigo)
PRODUCT_CREATE_ARGS.update(descricao)
