from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields

from model.entities import Empresa


class EmpresaSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Empresa

    id = fields.Str()
    nome_fantasia = auto_field()
    razao_social = auto_field()
    cnpj = auto_field()
    cnae = auto_field()
    data_situacao = auto_field()
    abertura = auto_field()
    situacao = auto_field()
    uf = auto_field()
    telefone = auto_field()
    bairro = auto_field()
    logradouro = auto_field()
    numero = auto_field()
    cep = auto_field()
    municipio = auto_field()
    complemento = auto_field()
    email = auto_field()
    created_at = auto_field()
    updated_at = auto_field()
