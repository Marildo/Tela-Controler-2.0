from sqlalchemy import func, Column
from sqlalchemy.types import DateTime,INTEGER

from model.config import Base


class BaseEntity(Base):
    __abstract__ = True

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
