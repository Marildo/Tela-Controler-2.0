from unittest import TestCase, main

from tests.helper import helper


class UserTest(TestCase):
    resource = '/usuarios'

    entity = {
        "password": "123456789",
        "nome": "Maria"
    }

    def test_should_return_401(self):
        url = helper.host + self.resource
        helper.assert_401(url)

    def test_should_return_200_and_list(self):
        helper.assert_200_and_list(self.resource)

    def test_should_return_200_and_one_entity(self):
        url = f'{self.resource}/{1}'
        helper.assert_200_and_entity(url)

    def test_should_return_201_and_entity_created(self):
        user = self.entity.copy()
        user.update({"email": f'{helper.generator_words(12)}@tela.com.br'})
        helper.assert_201_and_entity_created(self.resource, user)

    def test_should_return_422_entity_without_a_field(self):
        helper.assert_422_entity_without_a_field(self.resource, self.entity)

    def test_should_return_422_entity_with_an_unknown_field(self):
        helper.assert_422_entity_with_an_unknown_field(self.resource, self.entity)

    def test_should_return_200_and_entity_updated(self):
        nome = helper.generator_words(12)
        self.entity.update({'nome': nome})
        url = f'{self.resource}/{1}'
        response = helper.assert_200_and_entity_updated(url, self.entity)
        data = response.json()
        self.assertEqual(nome, data['data']['nome'])

    def test_should_return_422_entity_with_an_unknown_field_not_updated(self):
        url = f'{self.resource}/{1}'
        helper.assert_422_entity_with_an_unknown_field(url, self.entity, method='PUT')

    def test_should_return_200_entity_deleted(self):
        url = f'{self.resource}/{15}'
        helper.assert_200_entity_deleted(url)

    def test_should_return_200_and_password_updated(self):
        data = {'password': 'ABCDEFGHIJ'}
        url = f'{self.resource}/password/{5}'
        response = helper.make_request(method='PATCH', resource=url, json=data)
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    main(verbosity=2)
