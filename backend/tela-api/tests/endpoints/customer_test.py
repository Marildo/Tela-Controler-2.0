from unittest import TestCase, main

from tests.helper import helper


class CustomerTest(TestCase):
    resource = '/participantes'

    entity = {
        "nome": helper.generator_words(30),
        "fantasia": helper.generator_words(30),
    }

    def set_docs(self):
        self.entity.update({
            "cpf": helper.generator_cpf(),
            "cnpj": helper.generator_cnpj()
        })

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
        self.set_docs()
        helper.assert_201_and_entity_created(self.resource, self.entity)

    def test_should_return_422_entity_without_a_field_not_created(self):
        helper.assert_422_entity_without_a_field(self.resource, self.entity)

    def test_should_return_422_entity_invalid_cnpj_not_created(self):
        copy = self.entity.copy()
        copy.update({'cnpj': '830000000196'})
        response = helper.assert_422_entity_with_ivalid_field(self.resource, copy)
        data = response.json()
        self.assertEqual('CNPJ Inválido', data['data'][0]['error'])

    def test_should_return_422_entity_invalid_cpf_not_created(self):
        copy = self.entity.copy()
        copy.update({'cpf': '830000000196'})
        response = helper.assert_422_entity_with_ivalid_field(self.resource, copy)
        data = response.json()
        self.assertEqual('CPF Inválido', data['data'][0]['error'])

    def test_should_return_422_entity_with_an_unknown_field_not_created(self):
        helper.assert_422_entity_with_an_unknown_field(self.resource, self.entity)

    def test_should_return_200_and_entity_updated(self):
        fantasia = helper.generator_words(12)
        self.entity.update({"fantasia": fantasia})
        url = f'{self.resource}/{1}'
        response = helper.assert_200_and_entity_updated(url, self.entity)
        data = response.json()
        self.assertEqual(fantasia, data['data']['fantasia'])

    def test_should_return_422_entity_with_an_unknown_field_not_updated(self):
        url = f'{self.resource}/{1}'
        helper.assert_422_entity_with_an_unknown_field(url, self.entity, method='PUT')

    def test_deve_retorna_200_delete(self):
        url = f'{self.resource}/{15}'
        helper.assert_200_entity_deleted(url)


if __name__ == "__main__":
    main(verbosity=2)
