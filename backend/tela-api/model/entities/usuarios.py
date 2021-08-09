from sqlalchemy import Column, String, Integer
from .base_entity import BaseEntity


class Usuario(BaseEntity):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    nome = Column(String)
    password = Column(String, nullable=False)

    # empresa_id = relationship("empresas")