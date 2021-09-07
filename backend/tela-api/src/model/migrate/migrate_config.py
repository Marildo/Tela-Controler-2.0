import json
import os
import re
from datetime import datetime
from typing import Dict


class MigrateConfig:

    def __init__(self) -> None:
        self.filename = 'data.json'

    def add_company(self, cnpj: str) -> bool:
        data = self.__load_data()
        cnpj = re.sub(r'\D', '', str(cnpj))
        if cnpj in data['companies']:
            return False

        company = {
            'cnpj': int(cnpj),
            'version': 0
        }
        company.update(self.__updated_now())
        data['companies'].append(company)
        return self.__save_data(data)

    def __load_data(self) -> Dict:
        if not os.path.isfile(self.filename):
            data = {'master_version': 0}
            data.update(self.__updated_now())
            data.update({'companies': []})
            self.__save_data(data)

        with open(file=self.filename, mode='r') as file:
            return json.load(file)

    def __save_data(self, data: Dict) -> bool:
        with open(file=self.filename, mode='w') as file:
            json.dump(data, file)
            return True

    @staticmethod
    def __updated_now() -> Dict:
        return {'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
