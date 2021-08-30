from webargs import fields, validate

codigo = {'codigo': fields.Str(required=True, validate=[validate.Length(min=5, max=60)])}
descricao = {'descricao': fields.Str(required=True, validate=[validate.Length(min=5, max=250)])}

CREATE_PRODUCT_ARGS = dict()
CREATE_PRODUCT_ARGS.update(codigo)
CREATE_PRODUCT_ARGS.update(descricao)

UPDATE_PRODUCT_ARGS = dict()
UPDATE_PRODUCT_ARGS.update(codigo)
UPDATE_PRODUCT_ARGS.update(descricao)
