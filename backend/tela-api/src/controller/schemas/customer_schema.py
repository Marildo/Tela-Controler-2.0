from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields

from src.model.entities import Participante
from .address_schema import AddressSchema

class CustomerSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Participante

    id = auto_field()
    nome = auto_field()
    fantasia = auto_field()
    cnpj = auto_field()
    cpf = auto_field()
    enderecos = fields.Nested(AddressSchema, many=True)
  
   
