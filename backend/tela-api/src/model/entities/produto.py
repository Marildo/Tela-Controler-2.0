from sqlalchemy import Column, String, DECIMAL, INTEGER,DATETIME, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .base_entity import BaseEntity


class Produto(BaseEntity):
    __tablename__ = 'produtos'

    codigo = Column(String(30), unique=True, nullable=False)
    nome = Column(String(250), default='')
    cod_barras = Column(String(14), default='')
    referencia = Column(String(250), default='')
    observacao = Column(String(510), default='')

    pr_venda_vista = Column(DECIMAL(10, 2), default=0.01)
    pr_venda_prazo = Column(DECIMAL(10, 2), default=0.01)
    pr_custo = Column(DECIMAL(12,3))
    outros = Column(DECIMAL(12,3))

    estoque = Column(DECIMAL(12, 3), default=0.0)
    estoque_minimo = Column(DECIMAL(10, 2))

    unidade = Column(String(6), ForeignKey('unidades.unid'), nullable=False)
    qtd_embalagem = Column(DECIMAL(10,2), default=0.0)
    setor_id = Column(INTEGER, ForeignKey('setores.id'), nullable=False)
    setor = relationship('Setor')

    ultima_compra = Column(DATETIME)
    ultima_venda = Column(DATETIME)
    ativo = Column(Boolean, default=True, nullable=False)
