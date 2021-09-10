from telacore.utils import CNPJUtil, CPFUtil
from webargs import fields, validate


def validade_cpf(cpf: str) -> bool:
    if len(cpf) == 0:
        return True
    return CPFUtil.validate(cpf)


def validade_cnpj(cnpj: str) -> bool:
    if len(cpf) == 0:
        return True
    return CNPJUtil.validate(cnpj)


nome = {'nome': fields.Str(required=True, validate=[validate.Length(min=3, max=60)])}
fantasia = {'fantasia': fields.Str(validate=validate.Length(min=2, max=120))}
cnpj = {'cnpj': fields.Str(validate=validade_cnpj)}
cpf = {'cpf': fields.Str(validate=validade_cpf)}

CREATE_CUSTOMER_ARGS = {}
CREATE_CUSTOMER_ARGS.update(nome)
CREATE_CUSTOMER_ARGS.update(fantasia)
CREATE_CUSTOMER_ARGS.update(cnpj)
CREATE_CUSTOMER_ARGS.update(cpf)

UPDATE_CUSTOMER_ARGS = {}
UPDATE_CUSTOMER_ARGS.update(nome)
UPDATE_CUSTOMER_ARGS.update(fantasia)
UPDATE_CUSTOMER_ARGS.update(cnpj)
UPDATE_CUSTOMER_ARGS.update(cpf)
