from webargs import fields, validate

uf = {'uf': fields.Str(required=True, validate=validate.Length(min=2, max=2))}
ibge = {'ibge': fields.Int(required=True)}
cep = {'cep': fields.Str(required=True)}
logradouro = {'logradouro': fields.Str(required=True, validate=validate.Length(min=3, max=120))}
numero = {'numero': fields.Str(required=True, validate=validate.Length(min=1, max=10))}
complemento = {'complemento': fields.Str()}
bairro = {'bairro': fields.Str(required=True, validate=validate.Length(min=3, max=120))}
participante_id = {'participante_id': fields.Int(required=True)}


CREATE_ADDRESS_ARGS = {}
CREATE_ADDRESS_ARGS.update(uf)
CREATE_ADDRESS_ARGS.update(ibge)
CREATE_ADDRESS_ARGS.update(cep)
CREATE_ADDRESS_ARGS.update(logradouro)
CREATE_ADDRESS_ARGS.update(numero)
CREATE_ADDRESS_ARGS.update(complemento)
CREATE_ADDRESS_ARGS.update(bairro)
CREATE_ADDRESS_ARGS.update(participante_id)

UPDATE_ADDRESS_ARGS = {}
UPDATE_ADDRESS_ARGS.update(uf)
UPDATE_ADDRESS_ARGS.update(ibge)
UPDATE_ADDRESS_ARGS.update(cep)
UPDATE_ADDRESS_ARGS.update(logradouro)
UPDATE_ADDRESS_ARGS.update(numero)
UPDATE_ADDRESS_ARGS.update(complemento)
UPDATE_ADDRESS_ARGS.update(bairro)
UPDATE_ADDRESS_ARGS.update(participante_id)
