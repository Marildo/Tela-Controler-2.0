from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from src.model.entities import Endereco


class AddressSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Endereco

    id = auto_field()
    uf = auto_field()
    ibge = auto_field()
    cep = auto_field()
    logradouro = auto_field()
    numero = auto_field()
    complemento = auto_field()
    bairro = auto_field()
    participante_id = auto_field()
