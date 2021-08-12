from settings import Settings


class DBConfig:

    def __init__(self, cnpj: str):
        self.__data_base = f'emp_{cnpj}'
        self.__settings: Settings = Settings()

    @property
    def user(self) -> str:
        return self.__settings.get_database_user()

    @property
    def password(self) -> str:
        return self.__settings.get_database_password()

    @property
    def database(self) -> str:
        return self.__data_base

    @property
    def debug(self) -> bool:
        return self.__settings.get_debug()
