from unittest import TestCase, main

from src.telacore.utils import StrUtil


class StrUtilTest(TestCase):

    def test_normalize(self):
        text = 'Ação Usuário, Você, Antecipação'
        self.assertEqual('Acao Usuario, Voce, Antecipacao', StrUtil.normalize(text))


if __name__ == "__main__":
    main(verbosity=2)
