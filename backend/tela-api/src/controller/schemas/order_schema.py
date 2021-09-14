from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow_sqlalchemy.schema import auto_field

from src.model.entities import Pedido


class OrderSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Pedido

    id = auto_field()
    data = auto_field()
    total_produtos = auto_field()
    descontos = auto_field()
    outros = auto_field()
    total = auto_field()
    participante_id = auto_field()
    endereco_id = auto_field()
