from datetime import datetime


def br_parse_date(value: str) -> datetime:
    """
    Converte uma string no formato dia/mes/ano para datetime
    :param value: str
    :return: datetime
    """
    return datetime.strptime(value, '%d/%m/%Y')
