from sqlalchemy.sql.schema import ForeignKey
from src.model.entities import participante
from sqlalchemy import Column, String, Integer
from sqlalchemy.types import SMALLINT, CHAR

from .base_entity import BaseEntity


class Endereco(BaseEntity):
    __tablename__ = 'enderecos'

    uf = Column(CHAR(2), nullable=False)
    ibge = Column(Integer, default=0)
    cep = Column(String(10), default='')
    logradouro = Column(String(120), default='')
    numero = Column(String(10), default='')
    complemento = Column(String(120), default='')
    bairro = Column(String(120), default='')
    participante_id = Column(Integer, ForeignKey('participantes.id'))