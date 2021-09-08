import sys

from .migrate_config import MigrateConfig


#TODO - Controle de transações ao executar scripts
#TODO - Rodar migrate para todas as base de dados

def add_company(cnpj: str):
    migrate = MigrateConfig()
    migrate.add_company(cnpj)


if __name__ == '__main__':
    add_company(sys.argv[1])
