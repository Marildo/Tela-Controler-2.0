import json
from os import name

from typing import Dict


class MigrateConfig:

    def __init__(self) -> None:
        self.filename = 'data.json'

    def add_company(self, cnpj: str):
        data = self.load_data()
        company  = {
            'cnpj': cnpj,
            'version': 0
        }
        data['companies'].append(company)
        self.save_data(data)
       
       

    def load_data(self) -> Dict:
        with open(file=self.filename, mode='r') as file:
            data =  json.load(file)

        if 'companies' not in data:
            data['companies'] = []

        return data

    def save_data(self, data:Dict) -> bool:
        with open(file=self.filename, mode='w') as file:
            json.dump(data, file)