from sqlalchemy import Column, String, Boolean

from .base_entity import BaseEntity


class Setor(BaseEntity):
    __tablename__ = "setores"

    nome = Column(String(30), default='')
    ativo = Column(Boolean, default=True, nullable=False)
