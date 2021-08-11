import os
from abc import ABC, abstractmethod


class BaseSetting(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @staticmethod
    def _load_value(name, default=None):
        value = os.environ[name] if name in os.environ else default
        return value

    def get_api_port(self) -> int:
        return self._load_value('API_PORT', 3100)

    def get_debug(self) -> bool:
        value = self._load_value('DEBUG', 0)
        return value in ('1', 'True', 'Active')

    def get_level_log(self) -> str:
        return self._load_value('LEVEL_LOG', 'INFO')

    def get_database_timeout(self) -> int:
        return self._load_value('DATABASE_TIMEOUT', 1000)

    def get_database_host(self) -> str:
        return self._load_value('DATABASE_HOST', '')

    def get_database_user(self) -> str:
        return self._load_value('DATABASE_USER', '')

    def get_database_password(self) -> str:
        return self._load_value('DATABASE_PASSWORD', '')

    def get_database_port(self) -> int:
        return self._load_value('DATABASE_PORT', 3306)

    def get_database_master_name(self) -> str:
        return self._load_value('DATABASE_NAME', '')

    def get_database_charset(self) -> str:
        return self._load_value('DATABASE_CHARSET', 'utf8mb4')
