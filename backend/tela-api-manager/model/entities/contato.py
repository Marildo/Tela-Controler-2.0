from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String

from .base_entity import BaseEntity


class Contato(BaseEntity):
    __tablename__ = 'contatos'

    email = Column(String(255), default='')
    nome = Column(String(120), default='')
    client_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
