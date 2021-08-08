from sqlalchemy import Column, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import INTEGER, String
from sqlalchemy.types import DateTime

from model.config import Base


class Cliente(Base):
    __tablename__ = "clientes"

    uuid = Column(String(255), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    last_token = Column(DateTime, nullable=False, default=func.now())
    empresa_id = Column(INTEGER, ForeignKey('empresas.id'), nullable=False)
