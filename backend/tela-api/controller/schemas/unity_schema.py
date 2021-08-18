from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from model.entities import Unidade


class UnitySchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Unidade

    id = auto_field()
    unid = auto_field()
    descricao = auto_field()
    fracionavel = auto_field()
