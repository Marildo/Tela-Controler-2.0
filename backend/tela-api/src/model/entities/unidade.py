from sqlalchemy import Boolean
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String

from .base_entity import BaseEntity


class Unidade(BaseEntity):
    __tablename__ = 'unidades'

    unid = Column(String(4), unique=True, nullable=False, default='')
    descricao = Column(String(30), default='')
    fracionavel = Column(Boolean, default=False, nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)
