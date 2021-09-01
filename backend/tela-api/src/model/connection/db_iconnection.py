from abc import ABC, abstractmethod

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.config.base import Base
from model.config.db_config import DBConfig


class IDBConnection(ABC):

    def __init__(self, config: DBConfig):
        self._config: DBConfig = config
        self._session = None
        self._engine = None

    def __enter__(self):
        self._engine = create_engine(self._get_url(), echo=self._config.debug)
        self._session = sessionmaker()(bind=self._engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def close(self):
        self.session.close()
        self.engine.dispose()

    def init_db(self):
        Base.metadata.create_all(self.engine)

    @abstractmethod
    def _get_url(self) -> str:
        raise NotImplementedError

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine
