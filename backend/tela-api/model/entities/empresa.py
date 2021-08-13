from sqlalchemy import Column, String, Integer
from sqlalchemy.types import SMALLINT, CHAR

from .base_entity import BaseEntity


class Empresa(BaseEntity):
    __tablename__ = 'empresas'

    nome = Column(String(120), nullable=False)
    fantasia = Column(String(120), nullable=False)
    cnpj = Column(String(20), nullable=False, unique=True)
    cpf = Column(String(15))
    ie = Column(String(20))
    ie_st = Column(String(20))
    im = Column(String(30))
    cnae = Column(String(12))
    suframa = Column(String(15))
    pefil = Column(CHAR(1), default='A')
    ind_atividade = Column(SMALLINT, default=1)

    uf = Column(CHAR(2), nullable=False)
    ibge = Column(Integer)
    cep = Column(String(10))
    logradouro = Column(String(120))
    numero = Column(String(10))
    complemento = Column(String(120))
    bairro = Column(String(120))
    fone = Column(String(15))
    celular = Column(String(15))
    email = Column(String(120))
