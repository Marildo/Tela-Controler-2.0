from sqlalchemy import Column, String, Integer, Date, BOOLEAN, CHAR
from .base_entity import BaseEntity


class Empresa(BaseEntity):
    __tablename__ = "empresas"

    cnpj = Column(String(15), unique=True, index=True)
    razao_social = Column(String(255), default='')
    nome_fantasia = Column(String(255), default='')
    cnae = Column(String(8))
    data_situacao = Column(Date)
    abertura = Column(Date)
    situacao = Column(BOOLEAN, default=True)
    uf = Column(CHAR(2))
    telefone = Column(String(60))
    bairro = Column(String(255), default='')
    logradouro = Column(String(255), default='')
    numero = Column(String(20), default='')
    cep = Column(String(12), default='')
    municipio = Column(String(255), default='')
    complemento = Column(String(255), default='')
    email = Column(String(255), default='')





