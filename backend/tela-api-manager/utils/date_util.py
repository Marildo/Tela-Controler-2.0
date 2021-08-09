from datetime import datetime

class DateUtil:

    @staticmethod
    def br_parse_date(value):
        return datetime.strptime(value, '%d/%m/%Y')
