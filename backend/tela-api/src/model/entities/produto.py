from sqlalchemy import Column, String, DECIMAL, INTEGER,Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .base_entity import BaseEntity


class Produto(BaseEntity):
    __tablename__ = 'produtos'

    codigo = Column(String(30), unique=True, nullable=False)
    nome = Column(String(250), default='')
    cod_barras = Column(String(14), default='')
    unidade = Column(String(6), ForeignKey('unidades.unid'))
    ncm = Column(String(8), default='')
    cest = Column(String(8), default='')
    aliq_icms = Column(DECIMAL(6, 3), default=0)

    setor_id = Column(INTEGER, ForeignKey('setores.id'), nullable=False)
    setor = relationship('Setor')
    ativo = Column(Boolean, default=True, nullable=False)