from sqlalchemy import Column, String

from .base_entity import BaseEntity


class Usuario(BaseEntity):
    __tablename__ = "usuarios"

    email = Column(String, nullable=False, unique=True)
    nome = Column(String)
    password = Column(String, nullable=False)
