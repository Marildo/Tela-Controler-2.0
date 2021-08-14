from model.config import Base
from sqlalchemy import Column, func
from sqlalchemy.types import INTEGER, DateTime


class BaseEntity(Base):
    __abstract__ = True

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False,
                        default=func.now(), onupdate=func.now())
