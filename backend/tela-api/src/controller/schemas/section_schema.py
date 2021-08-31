from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from src.model.entities import Setor


class SectionSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Setor

    id = auto_field()
    nome = auto_field()
    ativo = auto_field()
