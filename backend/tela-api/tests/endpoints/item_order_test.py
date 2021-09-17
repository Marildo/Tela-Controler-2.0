import json
from unittest import TestCase, main

from tests.helper import helper


class ItemOrderTest(TestCase):
    resource = '/pedidos_items'

    entity = {
        "qtd": 0.20,
        "descontos": 0.20,
        "outros": 0.10,
        "total": 10.0,
        "pedido_id": 1,
        "produto_id": 1
    }

    def setUp(self) -> None:
        helper.login()

    def test_should_return_201_and_entity_created(self):
        helper.assert_201_and_entity_created(self.resource, self.entity)

    def test_should_return_422_entity_without_a_field_not_created(self):
        helper.assert_422_entity_without_a_field(self.resource, self.entity)

    def test_should_return_422_entity_with_an_unknown_field_not_created(self):
        helper.assert_422_entity_with_an_unknown_field(self.resource, self.entity)

    def test_should_return_200_and_entity_updated(self):
        qtd = 2.99
        self.entity.update({"qtd": qtd})
        url = f'{self.resource}/{1}'
        response = helper.assert_200_and_entity_updated(url, self.entity)
        data = response.json()
        self.assertEqual(qtd, data['data']['qtd'])

    def test_should_return_422_entity_with_an_unknown_field_not_updated(self):
        url = f'{self.resource}/{1}'
        helper.assert_422_entity_with_an_unknown_field(url, self.entity, method='PUT')

    def test_deve_retorna_200_delete(self):
        url = f'{self.resource}/{15}'
        helper.assert_200_entity_deleted(url)


if __name__ == "__main__":
    main(verbosity=2)
