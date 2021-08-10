from unittest import TestCase, main

from src.telacore.utils import cnpj_util

cnpjs_validos = ['01082633000159', '12782079000139', '95794934000159', '84703578000102', '12452566000133']


class CNPJUtilTest(TestCase):

    def test_validade_deve_validar_cnpj_sem_mascara(self):
        result = cnpj_util.validate(cnpjs_validos[0])
        assert result

    def test_validade_nao_deve_validar_cnpj_sem_mascara(self):
        result = cnpj_util.validate('01082633000109')
        self.assertFalse(result)

    def test_enconde_and_decode(self):
        for cnpj in cnpjs_validos:
            with self.subTest(cnpj):
                encodec = cnpj_util.encode(cnpj)
                decoded = cnpj_util.decode(encodec)
                self.assertEqual(cnpj, decoded)


if __name__ == "__main__":
    main(verbosity=2)
