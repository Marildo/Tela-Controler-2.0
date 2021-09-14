from unittest import TestCase, main

from tests.helper import helper


class OrderTest(TestCase):
    resource = '/pedidos'

    entity = {
        "data": '2021-09-13 01:01:01',
        "descontos": 0.20,
        "outros": 0.10,
        "total_produtos": 10.0,
        "total": 10.10,
        "endereco_id": 1,
        "participante_id": 1
    }

    def setUp(self) -> None:
        helper.login()

    def test_should_return_401(self):
        url = helper.host + self.resource
        helper.assert_401(url)

    def test_should_return_403(self):
        url = helper.host + self.resource
        helper.assert_403(url)

    def test_should_return_200_and_list(self):
        helper.assert_200_and_list(self.resource)

    def test_should_return_200_and_one_entity(self):
        url = f'{self.resource}/{1}'
        helper.assert_200_and_entity(url)

    def test_should_return_201_and_entity_created(self):
        helper.assert_201_and_entity_created(self.resource, self.entity)

    def test_should_return_422_entity_without_a_field_not_created(self):
        helper.assert_422_entity_without_a_field(self.resource, self.entity)

    def test_should_return_422_entity_with_an_unknown_field_not_created(self):
        helper.assert_422_entity_with_an_unknown_field(self.resource, self.entity)

    def test_should_return_200_and_entity_updated(self):
        descontos = 2.00
        self.entity.update({"descontos": descontos})
        url = f'{self.resource}/{1}'
        response = helper.assert_200_and_entity_updated(url, self.entity)
        data = response.json()
        self.assertEqual(descontos, data['data']['descontos'])

    def test_should_return_422_entity_with_an_unknown_field_not_updated(self):
        url = f'{self.resource}/{1}'
        helper.assert_422_entity_with_an_unknown_field(url, self.entity, method='PUT')


if __name__ == "__main__":
    main(verbosity=2)
