from abc import ABC, abstractmethod

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.model.config.init_database import init_database
from src.model.config.db_config import DBConfig

# TODO - Tratar erros com muitas conexoes

class IDBConnection(ABC):

    def __init__(self, config: DBConfig):
        self._config: DBConfig = config
        self._engine = create_engine(self._get_url(), echo=True)  # self._config.debug)
        maker = sessionmaker()
        self._session = maker(bind=self._engine)
        #init_database(self._engine)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def close(self):
        self.session.close()
        self.engine.dispose()

    @abstractmethod
    def _get_url(self) -> str:
        raise NotImplementedError

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine
