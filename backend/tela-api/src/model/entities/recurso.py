from sqlalchemy import Column, String, Boolean

from .base_entity import BaseEntity


class Recurso(BaseEntity):
    __tablename__ = "recursos"

    nome = Column(String(60),  nullable=False, unique=True)
