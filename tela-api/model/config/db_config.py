from settings import Settings


class DBConfig:

    def __init__(self):
        self.__settings: Settings = Settings()

    @property
    def user(self) -> str:
        return self.__settings.get_database_user()

    @property
    def password(self) -> str:
        return self.__settings.get_database_password()

    @property
    def database_master(self) -> str:
        return self.__settings.get_database_master_name()

    @property
    def debug(self) -> bool:
        return self.__settings.get_debug()

