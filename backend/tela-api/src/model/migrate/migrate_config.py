import json
import logging
import os
import re
from datetime import datetime
from enum import Enum
from typing import Dict

from sqlalchemy import text

from model.config import DBConfig
from model.connection import DBConnection


class Action(Enum):
    UP = 'up'
    DOWN = 'down'


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

    def run(self, cnpj):
        data = self.__load_data()
        company = list(filter(lambda i: i['cnpj'] == cnpj, data['companies']))
        if not company:
            raise Exception('Company not found')
        company = company[0]

        version = company['version']
        while version < data['master_version']:
            version += 1
            self.__run_migrate(cnpj=cnpj, version=version)
            company.update({'version': version})
            company.update(self.__updated_now())
            self.__save_data(data)

    def __load_data(self) -> Dict:
        if not os.path.isfile(self.filename):
            data = {'master_version': 0}
            data.update(self.__updated_now())
            data.update({'companies': []})
            # self.__save_data(data)

        with open(file=self.filename, mode='r') as file:
            return json.load(file)

    def __save_data(self, data: Dict) -> bool:
        with open(file=self.filename, mode='w') as file:
            json.dump(data, file)
            return True

    @staticmethod
    def __updated_now() -> Dict:
        return {'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

    def __run_migrate(self, cnpj: str, version: int):
        logging.info('updating to ', version)
        script = self.__load_script(version=version, action=Action.UP)
        script = self.__prepare_script(script, cnpj)
        self.__execute_script(sql=script, cnpj=cnpj, version=version)
        logging.info('updated to ', version)

    def __load_script(self, version: int, action: Action) -> str:
        dirname = f'__{version:03d}__'
        current_path = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_path, 'scripts', dirname)
        files = os.listdir(script_path)
        file = [i for i in files if i.startswith(action.value)]
        if not file:
            raise Exception('Migrate file not found')

        file = os.path.join(script_path, file[0])
        with open(file, 'r') as sql_file:
            return sql_file.read()

    def __prepare_script(self, script: str, cnp: str) -> str:
        return script.replace('$data_base_name$', str(cnp))

    @staticmethod
    def __execute_script(sql: str, cnpj: int, version:int) -> int:
        config = DBConfig(None if version == 1 else cnpj )
        connection = DBConnection(config)
        with connection.engine.begin() as conn:
            conn.execute(text(sql))
