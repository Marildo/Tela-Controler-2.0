import logging


def config_logger(level: str = 'INFO'):
    logging.basicConfig(format='%(asctime)s - %(message)s', level=level)
