import random
import string
from typing import Dict, List
from unittest import TestCase

import requests

from settings import Settings


class Helper(TestCase):

    def __init__(self):
        super().__init__()
        setting = Settings()
        self.__host = f'http://127.0.0.1:{setting.get_api_port()}'
        self.__token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MzAzMjQwODgsInBheWxvYWQiOnsiaWQiOjEsIm5vbWUiOiJtYXJpYSIsImVtYWlsIjoibWFyaWEyQHBhaXZhLmNvbSIsImNvZGlnbyI6Ik1UTTBPVEF5TXprMk1qQXdOakF6T1E9PSJ9fQ.PHqQg8YkBNoCdCaABBjKuxnh8C9yafh2zknFuN21pt7ead7DV6hJEtkyYHvbSC76mdYV0kuD0IhKVZzueIWLjdxpG0uVw6QfD4yS3BszZrIylFRj8LwWWUITZPklACTtR5LIbJwIVL0YKRZTGmDrxFBgoXM-DRDi2f0d7KFi6v8GTLkB-WL8m7eyIIuy_D6TupMLpcn9KemTFFtiWNHEFfRaogRAuJivCPi2-48pwBC4JRMimAdq2mbQqTnB5JL3DDaP0JemvrnTcaTaQ4E1kUyaqAOvs1uEKCHyTtOy7p2Um7kbcVM2Dqy5Y8B2o1g_mW9_UeOh72srhyMv-q_G_A'

    @property
    def host(self):
        return self.__host

    @property
    def token(self):
        return self.__token

    def make_request(self, method: str, resource: str, json: Dict = {}) -> requests.Response:
        url = f'{self.__host}/{resource}'
        headers = {'Authorization': self.token}
        return requests.request(method=method, url=url, headers=headers, json=json)

    def assert_401(self, url: str) -> requests.Response:
        response = requests.get(url)
        self.assertEqual(401, response.status_code)
        return response

    def assert_200_and_list(self, url: str) -> requests.Response:
        response = self.make_request('GET', url)
        self.assertEqual(200, response.status_code)
        json = response.json()
        self.assertIsInstance(json['data'], List, 'Not is a list')
        return response

    def assert_200_and_entity(self, url: str) -> requests.Response:
        _id = 1
        response = self.make_request('GET', url)
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.assertEqual(_id, data['data']['id'])
        return response

    def assert_201_and_entity_created(self, url: str, entity: Dict) -> requests.Response:
        response = self.make_request(method='POST', resource=url, json=entity)
        data = response.json()
        if response.status_code != 201:
            print(data)
        self.assertEqual(201, response.status_code)
        self.assertTrue(data['data']['id'])
        return response

    def assert_200_and_entity_updated(self, url: str, entity: Dict) -> requests.Response:
        response = self.make_request(method='PUT', resource=url, json=entity)
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.assertTrue(data['data']['id'])
        return response

    def assert_422_entity_with_an_unknown_field(self, url: str, entity: Dict,
                                                method: str = 'POST') -> requests.Response:
        entity_copy = entity.copy()
        entity_copy.update({"unknown": "false"})
        response = helper.make_request(method=method, resource=url, json=entity_copy)
        self.assertEqual(422, response.status_code)
        return response

    def assert_422_entity_without_a_field(self, url: str, entity: Dict, method: str = 'POST') -> requests.Response:
        key = list(entity.keys())
        entity_copy = entity.copy()
        del entity_copy[key[0]]
        response = helper.make_request(method=method, resource=url, json=entity_copy)
        self.assertEqual(422, response.status_code)
        return response

    @staticmethod
    def generator_words(size: int, chars: str = string.ascii_uppercase) -> str:
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def generator_number(size: int, chars: str = string.digits) -> str:
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def generator_alpha(size: int, chars: str = string.ascii_uppercase + string.digits) -> str:
        return ''.join(random.choice(chars) for _ in range(size))


helper = Helper()
