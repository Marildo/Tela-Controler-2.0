from sqlalchemy import Column, String, Integer
from sqlalchemy.types import SMALLINT, CHAR

from .base_entity import BaseEntity


class Empresa(BaseEntity):
    __tablename__ = 'empresas'

    nome = Column(String(120), nullable=False)
    fantasia = Column(String(120), nullable=False)
    cnpj = Column(String(20), nullable=False, unique=True)
    cpf = Column(String(15), default='')
    ie = Column(String(20), default='')
    ie_st = Column(String(20), default='')
    im = Column(String(30), default='')
    cnae = Column(String(12), default='')
    suframa = Column(String(15), default='')
    perfil = Column(CHAR(1), default='A')
    ind_atividade = Column(SMALLINT, default=1)

    uf = Column(CHAR(2), nullable=False)
    ibge = Column(Integer, default=0)
    cep = Column(String(10), default='')
    logradouro = Column(String(120), default='')
    numero = Column(String(10), default='')
    complemento = Column(String(120), default='')
    bairro = Column(String(120), default='')
    fone = Column(String(15), default='')
    celular = Column(String(15), default='')
    email = Column(String(120), default='')
