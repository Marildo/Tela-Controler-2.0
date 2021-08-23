from sqlalchemy import Column, String

from .base_entity import BaseEntity


class Usuario(BaseEntity):
    __tablename__ = "usuarios"

    email = Column(String(255), nullable=False, unique=True)
    nome = Column(String(255))
    password = Column(String(255), nullable=False)
