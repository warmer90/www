import requests


class TestDeparment:

    def setup(self):
        corpid = "ww45f0b3e1f0fb5929"
        corpsecret = "7wpuu89ZzNGxuwoKVnsoC7o3YN4q38hxdbS0IGFAMU4"
        param = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        r = requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=param)
        self.token=r.json()["access_token"]

    def test_creat_deparment(self):

        param = {
            "access_token": self.token}
        json={
           "name": "广州研发中心2",
           "name_en": "RDGZ1",
           "parentid": 1,
           "order": 1,
           "id": 2222
        }
        r = requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/department/create", params=param,json=json)
        print(r.json())
        assert r.json()['errcode']==0
    def test_update_deparment(self):
        param = {"access_token": self.token}
        json={
           "id": 2222,
           "name": "深圳",
           "name_en": "shenzhen",
           "parentid": 1,
           "order": 1
        }
        r=requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/department/update",params=param,json=json)
        assert r.json()['errcode']==0


    def test_delete_deparment(self):
        param = {"access_token": self.token,
                 "id":2222
                 }
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/delete",params=param)

        assert r.json()['errcode'] == 0
    def test_get_deparmetn_list(self):
        param = {"access_token": self.token

                 }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list", params=param)
        print(r.json()["department"])
        assert r.json()['errcode'] == 0
