from sqlalchemy import Column, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import INTEGER, String
from sqlalchemy.types import DateTime

from .base_entity import BaseEntity


class Cliente(BaseEntity):
    __tablename__ = "clientes"

    uuid = Column(String(255), unique=True)
    last_token = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
    empresa_id = Column(INTEGER, ForeignKey('empresas.id'), nullable=False)
    contatos = relationship('Contato')
