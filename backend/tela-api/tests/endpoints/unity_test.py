from unittest import TestCase, main

import requests

from ..helper import helper


class UnityTest(TestCase):
    url = f'{helper.host}/unidade'

    def test_deve_retorna_401(self):
        response = requests.get(self.url)
        self.assertFalse(response.status_code, 404)

    def test_deve_retorna_200_e_lista(self):
        response = requests.get(self.url)
        self.assertFalse(response.status_code, 200)
        json = response.json()
        self.assertIsInstance(json.data, {}, 'Response não é uma lista')


if __name__ == "__main__":
    main(verbosity=2)