from telacore.utils import CNPJUtil, CPFUtil
from webargs import fields, validate


def validade_cpf(cpf: str) -> bool:
    if len(cpf) == 0:
        return True
    return CPFUtil.validate(cpf)


CREATE_COMPANY_ARGS = {
    'email': fields.Email(required=True),
    'password': fields.Str(required=True, validate=[validate.Length(min=6, max=30)]),
    'nome': fields.Str(required=True, validate=[validate.Length(min=3, max=120)]),
    'codigo': fields.Str(required=True)
}

UPDATE_COMPANY_ARGS = {
    'id': fields.Int(),
    'nome': fields.Str(required=True, validate=validate.Length(min=4, max=120)),
    'fantasia': fields.Str(required=True, validate=validate.Length(min=2, max=120)),
    'cnpj': fields.Str(required=True, validate=CNPJUtil.validate),
    'cpf': fields.Str(validate=validade_cpf),
    'ie': fields.Str(),
    'ie_st': fields.Str(),
    'im': fields.Str(),
    'cnae': fields.Str(),
    'suframa': fields.Str(),
    'perfil': fields.Str(validate=validate.Length(max=1)),
    'ind_atividade': fields.Int(),
    'uf': fields.Str(required=True, validate=validate.Length(min=2, max=2)),
    'ibge': fields.Int(required=True),
    'cep': fields.Str(required=True),
    'logradouro': fields.Str(required=True, validate=validate.Length(min=4, max=120)),
    'numero': fields.Str(required=True, validate=validate.Length(min=1, max=10)),
    'complemento': fields.Str(),
    'bairro': fields.Str(required=True, validate=validate.Length(min=4, max=120)),
    'fone': fields.Str(),
    'celular': fields.Str(),
    'email': fields.Email()
}
