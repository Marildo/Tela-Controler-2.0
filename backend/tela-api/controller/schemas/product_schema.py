from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from model.entities import Produto


class ProductSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Produto

    id = auto_field()
    codigo = auto_field()
    descricao = auto_field()
    cod_barras = auto_field()
