from datetime import datetime
from unittest import TestCase, main

from src.telacore.utils import date_util


class DateUtilTest(TestCase):

    def test_br_parse_date(self):
        date_br = '09/08/2021'
        date_value = date_util.br_parse_date(date_br)
        assert date_value == datetime(2021, 8, 9)


if __name__ == "__main__":
    main(verbosity=2)
