import requests
import yaml

from interface_wechact.page.baseAPI import BaseApi


class WeWork(BaseApi):
    def get_token(self, corpsecret):
        corpid = "ww45f0b3e1f0fb5929"

        #放入到配置文件config.yaml
        # corpsecret = "7wpuu89ZzNGxuwoKVnsoC7o3YN4q38hxdbS0IGFAMU4"

        req = {"method": "get",
               "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
               "params": {"corpid": corpid, "corpsecret": corpsecret}
               }
        #使用自己封装的requests方法
        r = self.send_api(req)
        # r = requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=param)

        self.token = r.json()["access_token"]
        return self.token
