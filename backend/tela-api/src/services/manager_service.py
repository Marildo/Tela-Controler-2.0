import requests

from src.settings import Settings
from .interfaces import IManager


class Manager(IManager):

    @staticmethod
    def find_company(_cnpj: str):
        setting = Settings()
        base_url = setting.get_url_api_manager()
        url = f'{base_url}/empresa/{_cnpj}'
        data = requests.get(url).json()
        return data['data']
