from dotenv import load_dotenv
from telacore.decorators import singleton
from telacore.settings import BaseSetting, config_logger


@singleton
class Settings(BaseSetting):
    def __init__(self):
        load_dotenv()
        config_logger(self.get_level_log())

    def get_database_master_name(self) -> str:
        return self._load_value('DATABASE_NAME_MASTER', '')

    def get_url_api_manager(self) -> str:
        return self._load_value('URL_API_MANAGER', 'http://127.0.0.1:4000/')
