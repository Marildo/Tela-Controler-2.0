from sqlalchemy import Column, String, DECIMAL, INTEGER, ForeignKey
from sqlalchemy.orm import relationship

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

    setor_id = Column(INTEGER, ForeignKey('setores.id'), nullable=False)
    setor = relationship('Setor')
