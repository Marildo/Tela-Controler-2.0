from logging import info

import src.model.entities as tables
from .database import Base


def init_database(engine):
    type(tables)
    info('Inicializando database ')
    Base.metadata.create_all(bind=engine)
