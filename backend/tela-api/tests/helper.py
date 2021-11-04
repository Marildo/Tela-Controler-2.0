import random
import string
from typing import Dict, List
from unittest import TestCase

from requests import Response, request, get, post
from telacore.utils import CNPJUtil, CPFUtil

from settings import Settings


class Helper(TestCase):

    def __init__(self):
        super().__init__()
        setting = Settings()
        self.__host = f'http://127.0.0.1:{setting.get_api_port()}'

    @property
    def host(self):
        return self.__host

    @property
    def token(self):
        return self.__token

    def make_request(self, method: str, resource: str, json: Dict = {}) -> Response:
        url = f'{self.__host}/{resource}'
        headers = {'Authorization': self.token}
        return request(method=method, url=url, headers=headers, json=json)

    def assert_401(self, url: str) -> Response:
        response = get(url)
        self.__is405(response, 401)
        self.assertEqual(401, response.status_code)
        return response

    def assert_403(self, url: str) -> Response:
        headers = {'Authorization': self.token_forbidden()}
        response = get(url=url, headers=headers)
        self.__is405(response, 403)
        self.assertEqual(403, response.status_code)
        data = response.json()
        self.assertEqual('Operation not allowed for this user', data['data']['error']['description'])
        return response

    def assert_200_and_list(self, url: str) -> Response:
        response = self.make_request('GET', url)
        self.__is405(response, 200)
        self.assertEqual(200, response.status_code)
        json = response.json()
        self.assertIsInstance(json['data'], List, 'Not is a list')
        return response

    def assert_200_and_entity(self, url: str) -> Response:
        _id = 1
        response = self.make_request('GET', url)
        self.__is405(response, 200)
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.assertEqual(_id, data['data']['id'])
        return response

    def assert_201_and_entity_created(self, url: str, entity: Dict) -> Response:
        response = self.make_request(method='POST', resource=url, json=entity)
        self.__is405(response, 201)
        data = response.json()
        if response.status_code != 201:
            print(data)
        self.assertEqual(201, response.status_code)
        self.assertTrue(data['data']['id'])
        return response

    def assert_200_and_entity_updated(self, url: str, entity: Dict) -> Response:
        response = self.make_request(method='PUT', resource=url, json=entity)
        self.__is405(response, 200)

        data = response.json()
        if response.status_code != 200:
            print(data)

        self.assertTrue(data['data']['id'])
        return response

    def assert_422_entity_with_an_unknown_field(self, url: str, entity: Dict,
                                                method: str = 'POST') -> Response:
        entity_copy = entity.copy()
        entity_copy.update({"unknown": "false"})
        response = helper.make_request(method=method, resource=url, json=entity_copy)
        self.__is405(response, 200)
        self.assertEqual(422, response.status_code)
        return response

    def assert_422_entity_without_a_field(self, url: str, entity: Dict, method: str = 'POST') -> Response:
        key = list(entity.keys())
        entity_copy = entity.copy()
        del entity_copy[key[0]]
        response = helper.make_request(method=method, resource=url, json=entity_copy)
        self.__is405(response, 200)
        self.assertEqual(422, response.status_code)
        return response

    def assert_422_entity_with_ivalid_field(self, url: str, entity: Dict, method: str = 'POST') -> Response:
        response = helper.make_request(method=method, resource=url, json=entity)
        self.__is405(response, 200)
        self.assertEqual(422, response.status_code)
        return response

    def assert_200_entity_deleted(self, url) -> Response:
        response = helper.make_request('DELETE', url)
        self.__is405(response, 200)
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.assertTrue(str(data['data']['rows_affected']).isnumeric())
        return response

    def __is405(self, response: Response, expect):
        if response.status_code == 405:
            self.assertEqual(expect, response.status_code)

    def login(self):
        body = {"email": "maria2@paiva.com",
                "password": "tela@123456789",
                "codigo": "MTM0OTAyMzk2MjAwNjAzOQ=="}
        response = post(self.host + '/login', json=body)
        self.assertEqual(response.status_code, 200)
        self.__token = response.json()['token']

    def token_forbidden(self):
        body = {"email": "maria393@paiva.coymç",
                "password": "123456789",
                "codigo": "MTM0OTAyMzk2MjAwNjAzOQ=="}
        response = post(self.host + '/login', json=body)
        return response.json()['token']

    @staticmethod
    def generator_words(size: int, chars: str = string.ascii_uppercase) -> str:
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def generator_cpf() -> str:
        return CPFUtil.generate()

    @staticmethod
    def generator_cnpj() -> str:
        return CNPJUtil.generate()

    @staticmethod
    def choise_cnpj() -> str:
        cnpjs = ['14980173000128', '09457503000165', '27036981000183', '29210810000154', '04538470000164',
                 '10338109000197', '41010074000196', '09568990000133', '24474010000127', '24794967000150',
                 '39291564000166', '08757126000117', '34885438000116', '35716841000184',
                 '07884479000115', '09163352000132', '20950216000125', '22505019000122', '17289518000190',
                 '11175939000103', '22880357000144', '27550147000101', '22880357000144', '03304861000151',
                 '23749566000116', '24233908000103', '10763700000191', '23020712000178', '31847937000120',
                 '09396155000163', '31689218000129', '04077973000180', '30553090000109', '27252377000194',
                 '09233481000150', '35656942000107', '12699402000105', '01135806000150', '28750038000109',
                 '27431120000108', '08150713000143', '33968614000110', '11144772000113', '27808698000122',
                 '08343180000116', '41445712000100', '06080252000154', '33274730000130', '13281917000153',
                 '29038694000138', '22627609000128', '81327066000192', '03953892000133', '37244763000198',
                 '19250684000108', '13227469000100', '15221776000109', '10482163000101', '00035070000185',
                 '05796051000195', '31588253000151', '10764204000152', '11047913000180', '12361795000142',
                 '12859673000180', '05888398000168', '15120887000129', '29746410000168', '14879066000108',
                 '07731299000101', '51059004000267', '22708292000154', '13613000000109', '21928419000188',
                 '30399862000108', '35966097000176', '21269225000118', '03216530000160', '40283752000121',
                 '36352579000107', '05155854000160', '68312339000167', '13038295000137', '21678718000101',
                 '19878064000118', '03651678000122', '05192971000102', '04128944000108', '14437524000159',
                 '31499410000152', '20259082000109', '26434643000137', '28804350000120', '04931660000147',
                 '34365434000107', '29010897000116', '36275316000133', '92132786000119']
        return random.choice(cnpjs)

    @staticmethod
    def generator_number(size: int, chars: str = string.digits) -> str:
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def generator_alpha(size: int, chars: str = string.ascii_uppercase + string.digits) -> str:
        return ''.join(random.choice(chars) for _ in range(size))


helper = Helper()
