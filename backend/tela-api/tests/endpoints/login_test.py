from unittest import TestCase, main

import requests

from ..helper import helper


class LoginTest(TestCase):
    url = f'{helper.host}/login'

    def test_body_vazio_deve_retorna_401(self):
        body = {}
        response = requests.post(self.url, json=body)
        self.assertEqual(response.status_code, 401)

    def test_body_com_dados_invalidos_deve_retorna_401(self):
        body = {"email": "asdf@ghjk.com",
                "password": "123456789",
                "codigo": "ASDFGHJKLQWERT"}
        response = requests.post(self.url, json=body)
        self.assertEqual(response.status_code, 401)

    def test_deve_retorna_200(self):
        body = {"email": "maria2@paiva.com",
                "password": "123456789",
                "codigo": "MTM0OTAyMzk2MjAwNjAzOQ=="}
        response = requests.post(self.url, json=body)
        json = response.json()
        helper.token = json['token']
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    main(verbosity=2)
