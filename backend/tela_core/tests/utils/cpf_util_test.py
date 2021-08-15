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

from src.telacore.utils import CPFUtil
from webargs import ValidationError


class cpfUtilTest(TestCase):

    def test_validade_deve_validar_cnpf_sem_mascara(self):
        result = CPFUtil.validate('79609442021')
        assert result

    def test_validade_deve_validar_cnpf_com_mascara(self):
        result = CPFUtil.validate('249.053.730-00')
        assert result

    def test_validade_nao_deve_validar_cpf_e_nao_gerar_execao(self):
        result = CPFUtil.validate('79609442029', raise_exception=False)
        self.assertFalse(result)

    def test_validade_nao_deve_validar_cpf_e_gerar_ValidationError(self):
        with self.assertRaises(ValidationError):
            CPFUtil.validate('79609442029', raise_exception=True)

    def test_validade_nao_deve_validar_cpf_e_gerar_ValidationError(self):
        with self.assertRaises(ValidationError):
            CPFUtil.validate('79609442029', raise_exception=True)

    def test_mask(self):
        value = CPFUtil.mask('22896587071')
        expect = '228.965.870-71'
        self.assertEquals(value, expect)

    def test_mask_int_cpf_start_with_zero(self):
        value = CPFUtil.mask(3539879056)
        expect = '035.398.790-56'
        self.assertEquals(value, expect)

    def test_unmask(self):
        value = CPFUtil.unmask('035.398.790-56')
        expect = '03539879056'
        self.assertEquals(value, expect)


if __name__ == "__main__":
    main(verbosity=2)
