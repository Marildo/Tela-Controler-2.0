from sqlalchemy import func, Column, Integer
from sqlalchemy.types import DateTime

from src.model.config import Base


class BaseEntity(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
