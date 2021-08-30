from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from src.model.entities import Usuario


class UsuarioSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Usuario

    id = auto_field()
    email = auto_field()
    nome = auto_field()
