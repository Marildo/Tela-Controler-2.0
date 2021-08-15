from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from model.entities import Empresa


class EmpresaSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Empresa

    id = auto_field()
    nome = auto_field()
    fantasia = auto_field()
    cnpj = auto_field()
    cpf = auto_field()
    ie = auto_field()
    ie_st = auto_field()
    im = auto_field()
    cnae = auto_field()
    suframa = auto_field()
    perfil = auto_field()
    ind_atividade = auto_field()
    uf = auto_field()
    ibge = auto_field()
    cep = auto_field()
    logradouro = auto_field()
    numero = auto_field()
    complemento = auto_field()
    bairro = auto_field()
    fone = auto_field()
    celular = auto_field()
    email = auto_field()
