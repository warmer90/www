import requests


class TestToken():

    def test_token(self):
        corpid="ww45f0b3e1f0fb5929"
        corpsecret="7wpuu89ZzNGxuwoKVnsoC7o3YN4q38hxdbS0IGFAMU4"
        param={
            "corpid":corpid,
            "corpsecret":corpsecret
        }
        r = requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=param)
        print(r.json())

