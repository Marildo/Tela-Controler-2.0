from unittest import TestCase, main

import requests
from telacore.utils import CNPJUtil

from tests.helper import helper


class CompanyTest(TestCase):
    resource = '/empresa'

    entity = {
        "bairro": "RESIDENCIAL JARDIM YPE",
        "celular": "",
        "cep": "37.557-466",
        "cnae": "62.01-5-01",
        "cnpj": "40.879.514/0001-83",
        "complemento": "APT 1",
        "cpf": "",
        "email": "uaitechsistemas@gmail.com",
        "fantasia": "UAITECH SISTEMAS",
        "fone": "(35) 9802-3939",
        "ibge": 3152501,
        "id": 1,
        "ie": "1233",
        "ie_st": "",
        "im": "36589",
        "ind_atividade": 1,
        "logradouro": "R HAROLDO ERIK MADISON",
        "nome": "UAITECH DESENVOLVIMENTO E ACESSORIA EM SISTEMAS LTDA",
        "numero": "35",
        "perfil": "A",
        "suframa": "",
        "uf": "MG"
    }

    def setUp(self) -> None:
        helper.login()

    def test_should_return_403(self):
        url = f'{helper.host}/{self.resource}/{1}'
        helper.assert_403(url)

    def test_should_return_200_and_one_entity(self):
        url = f'{self.resource}/{1}'
        helper.assert_200_and_entity(url)

    def test_should_return_200_and_entity_updated(self):
        bairro = helper.generator_words(12)
        self.entity.update({"bairro": bairro})
        url = f'{self.resource}/{1}'
        response = helper.assert_200_and_entity_updated(url, self.entity)
        data = response.json()
        self.assertEqual(bairro, data['data']['bairro'])

    def test_should_return_422_entity_with_an_unknown_field_not_updated(self):
        url = f'{self.resource}/{1}'
        helper.assert_422_entity_with_an_unknown_field(url, self.entity, method='PUT')

    def test_should_return_201_and_entity_created(self):
        url = 'http://127.0.0.1:4000/cliente/'
        cnpj = helper.choise_cnpj()
        data = {
            "contato": "Contato_test",
            "email": f'{helper.generator_words(12)}@tela.com.br',
            "cnpj": cnpj
        }

        response = requests.post(url=url, json=data)
        if response.status_code == 201:
            url = f'{helper.host}/{self.resource}'
            data = response.json()['data']

            data.update({'nome': 'UserMaster', 'password': '123456789'})
            response = requests.post(url=url, json=data)
            data = response.json()['data']
            print(data)
            company_cnpj = data['company']['cnpj']
            self.assertEqual(company_cnpj, CNPJUtil.mask(cnpj))
        else:
            print(cnpj, response.json())


if __name__ == "__main__":
    main(verbosity=2)
