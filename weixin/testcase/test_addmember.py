from weixin.page.contact import Contact
from weixin.page.main import Main


class TestAddMember:

    def test_add_member(self):
        main = Main()
        assert "bear5" in main.goto_add_member().add_member().get_member()


