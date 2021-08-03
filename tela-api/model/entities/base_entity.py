from sqlalchemy import func, Column, Integer
from sqlalchemy.types import  DateTime

from model.config import Base


class BaseEntity(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    create_time = Column(DateTime, nullable=False, default=func.now())
    update_time = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
