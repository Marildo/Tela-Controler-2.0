import random
import string
from typing import Dict, List
from unittest import TestCase

from requests import Response, request, get, post

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
                "password": "123456789",
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
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(12))

    @staticmethod
    def generator_cnpj() -> str:
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(14))

    @staticmethod
    def generator_number(size: int, chars: str = string.digits) -> str:
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def generator_alpha(size: int, chars: str = string.ascii_uppercase + string.digits) -> str:
        return ''.join(random.choice(chars) for _ in range(size))


helper = Helper()
