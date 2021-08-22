from sqlalchemy import Column, String, DECIMAL

from .base_entity import BaseEntity


class Produto(BaseEntity):
    __tablename__ = 'produtos'

    codigo = Column(String(60), unique=True, nullable=False)
    descricao = Column(String(250), default='')
    cod_barras = Column(String(14), default='')
    unidade = Column(String(6))
    ncm = Column(String(8), default='')
    cest = Column(String(8), default='')
    aliq_icms = Column(DECIMAL(6, 3), default=0)


