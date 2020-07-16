from interface_wechact.page.user import User


class TestUser:
    def setup(self):
        self.user=User()
        self.token=self.user.get_token(self.user.load("config.yaml")["corpsecret"])

    def test_create_user(self):
        r=self.user.creat_user()

        assert r["errcode"]==0
    def test_get_user(self):
        r=self.user.get_user()
        print(r)
        assert r["errcode"] == 0

    def test_update_user(self):
        r=self.user.update_user()
        print(r)
        assert r["errcode"] == 0











