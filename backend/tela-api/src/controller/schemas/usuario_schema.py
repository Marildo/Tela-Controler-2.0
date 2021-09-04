from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow_sqlalchemy.fields import Nested
from src.model.entities import Usuario

from .permission_schema import PermissionShcema

class UsuarioSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Usuario

    id = auto_field()
    email = auto_field()
    nome = auto_field()
    permissoes = Nested(PermissionShcema, many=True)
