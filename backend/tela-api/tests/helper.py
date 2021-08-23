import os

from settings import Settings


class Helper:

    def __init__(self):
        setting = Settings()
        self.__host = f'http://127.0.0.1:{setting.get_api_port()}'

    @property
    def host(self):
        return self.__host

    @property
    def token(self):
        return os.environ.get('token', '')

    @token.setter
    def token(self, token):
        os.environ['DEBUSSY'] = token


helper = Helper()
