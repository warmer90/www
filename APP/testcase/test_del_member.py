import pytest

from APP.page.app import App


class TestDelMember:
    def setup(self):
        self.app = App()
        self.main = self.app.startapp().main()

    @pytest.mark.parametrize("name",['曹操18'])
    def test_del_member(self,name):

        self.main.goto_address().search_member(name).click_b().del_member()