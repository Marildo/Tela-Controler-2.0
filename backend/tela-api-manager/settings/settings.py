from dotenv import load_dotenv
from telacore.decorators import singleton
from telacore.settings import BaseSetting, config_logger


@singleton
class Settings(BaseSetting):

    def __init__(self):
        load_dotenv()
        config_logger(self.get_level_log())