import re

from requests import get


def search_from_cnpj(cnpj: str):
    value = re.sub(r'\D', '', str(cnpj))
    url = f'https://www.receitaws.com.br/v1/cnpj/{value}'
    data = get(url).json()
    return data
