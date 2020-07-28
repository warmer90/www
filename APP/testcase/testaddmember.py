import pytest


from APP.page.app import App



class TestAddMember:

    def setup(self):
        self.app=App()
        self.main=self.app.startapp().main()

    @pytest.mark.parametrize("user,gender,phonenum",[
                                 ("孙尚香1", "女", "19933332229"),
                                 ])
    def test_addmember(self,user,gender,phonenum):

        self.main.goto_address().add_member().click_memberadd().set_name(user).set_gender(gender).set_phonenum(phonenum).chick_save()