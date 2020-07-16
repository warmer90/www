from interface_wechact.page.wework import WeWork


class User(WeWork):
    def creat_user(self):
        req = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {"access_token": self.token},
            "json": {"userid": "zhangsan",
                     "name": "张三",
                     "alias": "jackzhang",
                     "mobile": "13800000000",
                     "department": [1, 2]
                     }
        }
        r = self.send_api(req)
        return r.json()

    def get_user(self):
        req={
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params" :{"access_token": self.token,
                       "userid":23320
            }
        }
        r =self.send_api(req)
        return r.json()


    def update_user(self):
        req={
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {"access_token": self.token},
            "json":{
                "userid": "zhangsan",
                "name": "李四",
                "department": [1],
                "order": [10]
            }
        }
        r=self.send_api(req)
        return r.json()