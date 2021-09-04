from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow_sqlalchemy.schema import auto_field

from src.model.entities import Permissao


class PermissionShcema(SQLAlchemySchema):
    class Meta:
        load_instance = True
        model = Permissao

    id = auto_field()
    c = auto_field()
    r = auto_field()
    u = auto_field()
    d = auto_field()
