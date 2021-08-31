from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow_sqlalchemy.fields import Nested
from .section_schema import SectionSchema
from src.model.entities import Produto


class ProductSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Produto

    id = auto_field()
    codigo = auto_field()
    descricao = auto_field()
    cod_barras = auto_field()
    setor = Nested(SectionSchema, exclude=('ativo',))
