from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base_entity import BaseEntity


class Permissao(BaseEntity):
    __tablename__ = 'permissoes'

    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    recurso_id = Column(Integer, ForeignKey('recursos.id'))
    c = Column(Boolean, default=True, nullable=False)
    r = Column(Boolean, default=True, nullable=False)
    u = Column(Boolean, default=True, nullable=False)
    d = Column(Boolean, default=True, nullable=False)
    recurso = relationship('Recurso')