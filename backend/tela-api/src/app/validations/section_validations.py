from webargs import fields, validate

nome = {'nome': fields.Str(required=True, validate=[validate.Length(min=1, max=30)])}
ativo = {'ativo': fields.Boolean()}

CREATE_SECTION_ARGS = {}
CREATE_SECTION_ARGS.update(nome)
CREATE_SECTION_ARGS.update(ativo)

UPDATE_SECTION_ARGS = {
    'id': fields.Int()
}

UPDATE_SECTION_ARGS.update(nome)
UPDATE_SECTION_ARGS.update(ativo)


