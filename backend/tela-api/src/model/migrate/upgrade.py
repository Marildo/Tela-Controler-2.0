from model.migrate.migrate_config import MigrateConfig


def start(cnpj: str):
    migrate = MigrateConfig()
    migrate.run(cnpj)


start(7886699)
