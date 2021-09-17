from webargs import fields, validate

qtd = {'qtd': fields.Decimal(required=True, validate=[validate.Range(min=0.01)])}
descontos = {'descontos': fields.Decimal(required=True)}
outros = {'outros': fields.Decimal(required=True)}
total = {'total': fields.Decimal(required=True, validate=[validate.Range(min=0.01)])}
produto_id = {'produto_id': fields.Int(required=True)}
pedido_id = {'pedido_id': fields.Int(required=True)}

CREATE_ITEM_ORDER_ARGS = {}
CREATE_ITEM_ORDER_ARGS.update(qtd)
CREATE_ITEM_ORDER_ARGS.update(descontos)
CREATE_ITEM_ORDER_ARGS.update(outros)
CREATE_ITEM_ORDER_ARGS.update(total)
CREATE_ITEM_ORDER_ARGS.update(produto_id)
CREATE_ITEM_ORDER_ARGS.update(pedido_id)

UPDATE_ITEM_ORDER_ARGS = {
    'id': fields.Int()
}

UPDATE_ITEM_ORDER_ARGS.update(qtd)
UPDATE_ITEM_ORDER_ARGS.update(descontos)
UPDATE_ITEM_ORDER_ARGS.update(outros)
UPDATE_ITEM_ORDER_ARGS.update(total)
UPDATE_ITEM_ORDER_ARGS.update(produto_id)
UPDATE_ITEM_ORDER_ARGS.update(pedido_id)
