import json
import logging
import os
import re
from datetime import datetime
from enum import Enum
from typing import Dict, List, Tuple

from sqlalchemy import text

from src.model.config import DBConfig
from src.model.connection import DBConnection


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

    def upgrade(self, cnpj):
        company, data = self.__find_company(cnpj)
        version = company['version']
        while version < data['master_version']:
            version += 1
            self.__run_migrate(cnpj=cnpj, version=version, action=Action.UP)
            company.update({'version': version})
            company.update(self.__updated_now())
            self.__save_data(data)

    def downgrade(self, cnpj):
        company, data = self.__find_company(cnpj)
        version = company['version']
        if version == 0:
            return
        self.__run_migrate(cnpj=cnpj, version=version, action=Action.DOWN)
        version -= 1
        company.update({'version': version})
        company.update(self.__updated_now())
        self.__save_data(data)

    def __find_company(self, cnpj) -> Tuple:
        data = self.__load_data()
        company = list(filter(lambda i: i['cnpj'] == cnpj, data['companies']))
        if not company:
            raise Exception('Company not found')
        return company[0], data

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

    def __run_migrate(self, cnpj: str, version: int, action: Action):
        logging.info('updating to ', version)
        script = self.__load_script(version=version, action=action)
        scripts = self.__prepare_script(script, cnpj)
        self.__execute_script(scripts=scripts, cnpj=cnpj, version=version)
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

    @staticmethod
    def __prepare_script(script: str, cnp: str) -> List[str]:
        return script \
            .replace('$data_base_name$', str(cnp)) \
            .split(';')
        # .replace('\t', '') \
        # .replace('\n', '')

    @staticmethod
    def __execute_script(scripts: List[str], cnpj: str, version: int) -> int:
        result = 0
        config = DBConfig(cnpj=None if version == 1 else cnpj, autocommit=False)
        connection = DBConnection(config)
        with connection.engine.connect() as conn:
            with conn.begin() as transition:
                try:
                    for sql in scripts:
                        if sql:
                            r = conn.execute(text(sql))
                            result += r.rowcount
                    transition.commit()
                except Exception as error:
                    transition.rollback()
                    raise error

        return result
