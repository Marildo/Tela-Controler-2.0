from unittest import TestCase
import src.tela_utils.cnpj_util as cnpjUtil

class CNPJUtilTest(TestCase):

    def test_validade_deve_validar_cnpj_sem_mascara(self):
        cnpj = '01082633000159'
        result = cnpjUtil.validate(cnpj)
        assert result