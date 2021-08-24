import random
import string
from typing import Dict

import requests

from settings import Settings


class Helper:

    def __init__(self):
        setting = Settings()
        self.__host = f'http://127.0.0.1:{setting.get_api_port()}'
        self.__token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2Mjk5MjAxNDYsInBheWxvYWQiOnsiZW1haWwiOiJtYXJpYTJAcGFpdmEuY29tIiwibm9tZSI6Im1hcmlhIiwiaWQiOjEsImNvZGlnbyI6Ik1UTTBPVEF5TXprMk1qQXdOakF6T1E9PSJ9fQ.PAms8UYf4jPXdPgHHTvLFVbdOSxUWfxUbt9xSnyngEQ0nZSIrpMqx2-87e-0ufk9PBK8PkBCPOOyaK0bWDDtMMlniv3fvTYb0Y-0p555TwJkEruh8fOB9rin8hgra-q3qhMTOHua0BKl4PrTLEXSXrUTUlNBJuoFVc1WGwH4LU0riFCN1SJiNnOzlNQlmqupvyZm599xl_wslAP-8NbsXsR4LgycTArOA9G7bF4jhV_05KLDK2FelVCe2n3B38F2fE1Lk77nk5XUXUZFw6om0Fzrk4S2f1rj9rXibkfJ9F66LTmebTqYX9sSv-zdljHwnM3ZS0mdQa67VTbjZuHHuw'

    @property
    def host(self):
        return self.__host

    @property
    def token(self):
        return self.__token

    def make_request(self, method: str, resource: str, json: Dict = {}):
        url = f'{self.__host}/{resource}'
        headers = {'Authorization': helper.token}
        return requests.request(method=method, url=url, headers=headers, json=json)

    @staticmethod
    def generator_words(size: int, chars: str = string.ascii_uppercase + string.digits) -> str:
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def generator_number(size: int, chars: str = string.digits) -> str:
        return ''.join(random.choice(chars) for _ in range(size))


helper = Helper()
