from sqlalchemy import Column, String, Integer
from sqlalchemy.types import SMALLINT, Boolean

from .base_entity import BaseEntity


class Participante(BaseEntity):
    __tablename__ = 'participantes'

    nome = Column(String(120), nullable=False)
    fantasia = Column(String(120), nullable=False)
    cnpj = Column(String(20),default='', unique=True)
    cpf = Column(String(15), default='', unique=True)
    ativo = Column(Boolean, default=True, nullable=False)
