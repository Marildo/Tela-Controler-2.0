from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Float, Integer

from .base_entity import BaseEntity


class Pedido(BaseEntity):
    __tablename__ = 'pedidos'

    data = Column(DateTime)
    total_produtos = Column(Float, default=0)
    descontos = Column(Float, default=0)
    outros = Column(Float, default=0)
    total = Column(Float, default=0)
    participante_id = Column(Integer, ForeignKey('participantes.id'), nullable=False)
    endereco_id = Column(Integer, ForeignKey('enderecos.id'))
