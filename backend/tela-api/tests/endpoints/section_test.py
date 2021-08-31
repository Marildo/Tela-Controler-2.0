from unittest import TestCase, main

from tests.helper import helper


class SectionTest(TestCase):
    resource = '/setores'

    entity = {
        "nome": helper.generator_words(10)
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
        self.entity.update({'ativo': 'True'})
        helper.assert_201_and_entity_created(self.resource, self.entity)

    def test_should_return_422_entity_without_a_field_not_created(self):
        helper.assert_422_entity_without_a_field(self.resource, self.entity)

    def test_should_return_422_entity_with_an_unknown_field_not_created(self):
        helper.assert_422_entity_with_an_unknown_field(self.resource, self.entity)

    def test_should_return_200_and_entity_updated(self):
        self.entity.update({"ativo": "False"})
        url = f'{self.resource}/{1}'
        response = helper.assert_200_and_entity_updated(url, self.entity)
        data = response.json()
        self.assertEqual(False, data['data']['ativo'])

    def test_should_return_422_entity_with_an_unknown_field_not_updated(self):
        url = f'{self.resource}/{1}'
        helper.assert_422_entity_with_an_unknown_field(url, self.entity, method='PUT')

    def test_deve_retorna_200_delete(self):
        url = f'{self.resource}/{15}'
        helper.assert_200_entity_deleted(url)


if __name__ == "__main__":
    main(verbosity=2)
