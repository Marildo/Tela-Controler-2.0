import re
from typing import Dict

import requests


class CEPUtil:

    @staticmethod
    def find_cep(cep: str) -> Dict:
        cep = re.sub(r'\D', '', str(cep))
        url = f'https://viacep.com.br/ws/{cep}/json/'
        data = requests.get(url)
        return data.json() if data.ok else None
