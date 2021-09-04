from sqlalchemy import Column, Integer, Boolean, ForeignKey

from .base_entity import BaseEntity


class Permissao(BaseEntity):
    __tablename__ = 'permissoes'

    usuario_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    recurso_id = Column(Integer, ForeignKey('recursos.id'), primary_key=True)
    c = Column(Boolean, default=True, nullable=False)
    r = Column(Boolean, default=True, nullable=False)
    u = Column(Boolean, default=True, nullable=False)
    d = Column(Boolean, default=True, nullable=False)
