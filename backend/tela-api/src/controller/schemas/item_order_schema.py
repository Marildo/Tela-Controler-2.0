from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow_sqlalchemy.schema import auto_field

from src.model.entities import ItensPedido


class ItemOrderSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = ItensPedido

    id = auto_field()
    qtd = auto_field()
    descontos = auto_field()
    outros = auto_field()
    total = auto_field()
