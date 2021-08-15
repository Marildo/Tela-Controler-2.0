from unittest import TestCase, main

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../../src'
            )
        )
    )
except:
    raise

from src.telacore.utils import CNPJUtil
from webargs import ValidationError

cnpjs_validos = ['01082633000159', '12782079000139',
                 '95794934000159', '84703578000102', '12452566000133']


class CNPJUtilTest(TestCase):

    def test_validade_deve_validar_cnpj_sem_mascara(self):
        result = CNPJUtil.validate(cnpjs_validos[0])
        assert result

    def test_validade_nao_deve_validar_cnpj_e_nao_gerar_execao(self):
        result = CNPJUtil.validate('01082633000109', raise_exception=False)
        self.assertFalse(result)

    def test_validade_nao_deve_validar_cnpj_e_gerar_ValidationError(self):
        with self.assertRaises(ValidationError):
            CNPJUtil.validate('01082633000109', raise_exception=True)

    def test_validade_nao_deve_validar_cnpj_sem_mascara(self):
        result = CNPJUtil.validate('01082633000109')
        self.assertFalse(result)

    def test_enconde_and_decode(self):
        for cnpj in cnpjs_validos:
            with self.subTest(cnpj):
                encodec = CNPJUtil.encode(cnpj)
                decoded = CNPJUtil.decode(encodec)
                self.assertEqual(cnpj, decoded)

    def test_mask(self):
        value = CNPJUtil.mask('17346434000140')
        expect = '17.346.434/0001-40'
        self.assertEquals(value, expect)

    def test_mask_int_cnpj(self):
        value = CNPJUtil.mask(17346434000140)
        expect = '17.346.434/0001-40'
        self.assertEquals(value, expect)

    def test_mask_int_cnpj_start_with_zero(self):
        value = CNPJUtil.mask(7686822000117)
        expect = '07.686.822/0001-17'
        self.assertEquals(value, expect)

    def test_unmask(self):
        value = CNPJUtil.unmask('17.346.434/0001-40')
        expect = '17346434000140'
        self.assertEquals(value, expect)

    def test_unmask_int_cnpj(self):
        value = CNPJUtil.unmask(17346434000140)
        expect = '17346434000140'
        self.assertEquals(value, expect)

    def test_unmask_int_cnpj_start_with_zero(self):
        value = CNPJUtil.unmask('07.686.822/0001-17')
        expect = '07686822000117'
        self.assertEquals(value, expect)


if __name__ == "__main__":
    main(verbosity=2)
