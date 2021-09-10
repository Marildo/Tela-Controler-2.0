from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from src.model.entities import Participante


class CustomerSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Participante

    id = auto_field()
    nome = auto_field()
    fantasia = auto_field()
    cnpj = auto_field()
    cpf = auto_field()
   
