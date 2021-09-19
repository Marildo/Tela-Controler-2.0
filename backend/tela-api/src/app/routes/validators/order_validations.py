from webargs import fields, validate

data = {'data': fields.DateTime(required=True)}
total_produtos = {'total_produtos': fields.Decimal(required=True)}
descontos = {'descontos': fields.Decimal(required=True)}
outros = {'outros': fields.Decimal(required=True)}
total = {'total': fields.Decimal(required=True, validate=[validate.Range(min=0.01)])}
participante_id = {'participante_id': fields.Int(required=True)}
endereco_id = {'endereco_id': fields.Int(required=True)}

CREATE_ORDER_ARGS = {}
CREATE_ORDER_ARGS.update(data)
CREATE_ORDER_ARGS.update(total_produtos)
CREATE_ORDER_ARGS.update(descontos)
CREATE_ORDER_ARGS.update(outros)
CREATE_ORDER_ARGS.update(total)
CREATE_ORDER_ARGS.update(participante_id)
CREATE_ORDER_ARGS.update(endereco_id)

UPDATE_ORDER_ARGS = {
    'id': fields.Int()
}

UPDATE_ORDER_ARGS.update(data)
UPDATE_ORDER_ARGS.update(total_produtos)
UPDATE_ORDER_ARGS.update(descontos)
UPDATE_ORDER_ARGS.update(outros)
UPDATE_ORDER_ARGS.update(total)
UPDATE_ORDER_ARGS.update(participante_id)
UPDATE_ORDER_ARGS.update(endereco_id)
