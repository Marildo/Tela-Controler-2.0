import sys

from migrate_config import MigrateConfig


def add_company(cnpj: str):
    migrate = MigrateConfig()
    migrate.add_company(cnpj)


if __name__ == '__main__':
    add_company(sys.argv[1])
