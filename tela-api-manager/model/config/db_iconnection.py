from abc import ABC, abstractmethod

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .db_config import DBConfig


class IDBConnection(ABC):

    def __init__(self, config: DBConfig):
        self._config: DBConfig = config
        self._session = None

    def __enter__(self):
        engine = self.get_engine()
        session_maker = sessionmaker()
        self._session = session_maker(bind=engine, expire_on_commit=False)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()

    def get_engine(self):
        return create_engine(self._get_url(), echo=True)#self._config.debug)

    @abstractmethod
    def _get_url(self) -> str:
        raise NotImplementedError

    @property
    def session(self):
        return self._session
