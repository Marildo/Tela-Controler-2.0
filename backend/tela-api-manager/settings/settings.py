from telacore.decorators import singleton
from telacore.settings import BaseSetting


@singleton
class Settings(BaseSetting):
    pass
