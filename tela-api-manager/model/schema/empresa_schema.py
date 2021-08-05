from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from model.entities import Empresa


class EmpresaSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Empresa

    id = auto_field()
    nome_fantasia = auto_field()
    razao_social = auto_field()
