from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float, Integer, String

from .base_entity import BaseEntity


class ItensPedido(BaseEntity):
    __tablename__ = 'itens_pedido'

    qtd = Column(Float, default=0)
    descontos = Column(Float, default=0)
    outros = Column(Float, default=0)
    total = Column(Float, default=0)
    observacao = Column(String(250))
    pedido_id = Column(Integer, ForeignKey('pedidos.id'), nullable=False)
    produto_id = Column(Integer, ForeignKey('produtos.id'), nullable=False)
