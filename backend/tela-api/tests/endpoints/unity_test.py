from typing import List
from unittest import TestCase, main

import requests

from ..helper import helper


class UnityTest(TestCase):
    url = f'{helper.host}/unidades'
    resource = '/unidades'

    def test_deve_retorna_401(self):
        response = requests.get(self.url)
        self.assertEqual(401, response.status_code)

    def test_deve_retorna_200_e_lista(self):
        response = helper.make_request('GET', self.resource)
        self.assertEqual(200, response.status_code)
        json = response.json()
        self.assertIsInstance(json['data'], List, 'Not is a list')

    def test_deve_retorna_200_e_uma_unidade(self):
        _id = 1
        response = helper.make_request('GET', f'{self.resource}/{_id}')
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.equal = self.assertEqual(_id, data['id'])

    def test_deve_retorna_201_create_unidade(self):
        unid = {
            "unid": helper.generator_words(4),
            "descricao": "Unidade Teste",
            "fracionavel": "True"
        }
        response = helper.make_request(method='POST', resource=self.resource, json=unid)
        data = response.json()
        self.assertEqual(201, response.status_code)
        self.assertTrue(str(data['data']['id']).isnumeric())

    def test_deve_retorna_422_create_unidade_sem_unit(self):
        unid = {
            "descricao": "Unidade Teste",
            "fracionavel": "True"
        }
        response = helper.make_request(method='POST', resource=self.resource, json=unid)
        self.assertEqual(422, response.status_code)

    def test_deve_retorna_422_create_unidade_com_campo_desconhecido(self):
        unid = {
            "unid": "UNIT",
            "descricao": "Unidade Teste",
            "fracionavel": "True",
            "impostor": 'false'
        }
        response = helper.make_request(method='POST', resource=self.resource, json=unid)
        self.assertEqual(422, response.status_code)

    def test_deve_retorna_200_update_unidade(self):
        unid = {
            "unid": helper.generator_words(4),
            "descricao": "Unidade Teste",
            "fracionavel": "True",
            "ativo": "False",
        }
        _id = 1
        response = helper.make_request(method='PUT', resource=f'{self.resource}/{_id}', json=unid)
        data = response.json()
        self.assertEqual(200, response.status_code)
        self.assertTrue(str(data['data']['id']).isnumeric())
        self.assertFalse(data['data']['ativo'])

    def test_deve_retorna_200_delete_unidade(self):
        _id = 15
        response = helper.make_request('DELETE', f'{self.resource}/{_id}')
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.assertTrue(str(data['data']['rows_affected']).isnumeric())


if __name__ == "__main__":
    main(verbosity=2)
