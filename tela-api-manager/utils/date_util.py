from datetime import datetime


def str_br_to_date(value):
    return datetime.strptime(value, '%d/%m/%Y')
