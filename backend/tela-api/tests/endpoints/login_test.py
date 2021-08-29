from unittest import TestCase, main

import requests

from tests.helper import helper


class LoginTest(TestCase):
    url = f'{helper.host}/login'

    def test_should_return_401_empty_body(self):
        body = {}
        response = requests.post(self.url, json=body)
        self.assertEqual(response.status_code, 401)

    def test_should_return_401_invalid_login(self):
        body = {"email": "asdf@ghjk.com",
                "password": "123456789",
                "codigo": "ASDFGHJKLQWERT"}
        response = requests.post(self.url, json=body)
        self.assertEqual(response.status_code, 401)

    def test_should_return_200_and_token(self):
        body = {"email": "maria2@paiva.com",
                "password": "123456789",
                "codigo": "MTM0OTAyMzk2MjAwNjAzOQ=="}
        response = requests.post(self.url, json=body)
        self.assertEqual(response.status_code, 200)
        print(response.json()['token'])


if __name__ == "__main__":
    main(verbosity=2)
