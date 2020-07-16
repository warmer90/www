from weixin.page.main import Main


class TestAddDeparment:

    def test_add_dep(self):
        main=Main()
        main.goto_add_dep().add_dep()