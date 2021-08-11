from telacore.settings import BaseSetting


class TestSetting(BaseSetting):
    pass


def test():
    t = TestSetting()
    print(t.get_level_log())


test()
