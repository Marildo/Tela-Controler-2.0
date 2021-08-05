from requests import get


def search_from_cnpj(cnpj: str):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    data = get(url).json()
    return data
