import sys

from migrate_config import MigrateConfig


def add_company(cnpj: str):
    print(cnpj)
    migrate = MigrateConfig()
    migrate.add_company(cnpj)


if __name__ == '__main__':
    print('Estou no modulo', sys.argv)
    add_company(sys.argv[1])
