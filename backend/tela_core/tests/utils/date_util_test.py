from unittest import TestCase
from src.tela_utils.date_util import br_parse_date

from datetime import datetime
class DateUtilTest(TestCase):

    def test_br_parse_date(self):
        date_br = '09/08/2021'
        date_value = br_parse_date(date_br)
        assert date_value == datetime(2021, 8, 9)

