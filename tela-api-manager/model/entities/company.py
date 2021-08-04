from sqlalchemy import Column, String, Integer, Date, BOOLEAN
from .base_entity import BaseEntity


class Empresa(BaseEntity):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True)
    cnpj = Column(String(15), primary_key=True)
    razao_social = Column(String(255), default='')
    nome_fantasia = Column(String(255), default='')
    data_situacao = Column(Date)
    abertura = Column(Date)
    situacao = Column(BOOLEAN, default=True)

