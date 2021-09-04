from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from src.model.entities import Setor


class ResourceSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Setor

    id = auto_field()
    nome = auto_field()
