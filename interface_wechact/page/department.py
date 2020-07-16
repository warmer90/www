

from interface_wechact.page.wework import WeWork


class Department(WeWork):

    # 创建标签
    def create_tag(self, tagname, tagid):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/create",
            "params": {"access_token": self.token},
            "json": {"tagname": tagname, "tagid": tagid}
        }

        # parm={"access_token": self.token}
        # json={
        #        "tagname": "www",
        #        "tagid": 123
        #     }
        # r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/tag/create",params=parm,json=json)
        r = self.send_api(req)
        return r.json()

    # 更新标签
    def update_tag(self, tagname, tagid):
        # parm = {"access_token": self.token}
        # json = {
        #     "tagname": tagname,
        #     "tagid": tagid }
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/update",
            "params": {"access_token": self.token},
            "json": {"tagname": tagname, "tagid": tagid}
        }

        r = self.send_api(req)
        # r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/tag/update", params=parm, json=json)
        return r.json()

    # 删除标签
    def delete_tag(self, tagid):
        # parm = {"access_token": self.token,"tagid": 123 }

        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
            "params": {"access_token": self.token, "tagid": tagid},
        }
        r = self.send_api(req)
        # r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/tag/delete", parm)
        return r.json()

    # 获取标签成员
    def get_tag_member(self, tagid):
        # parm = {"access_token": self.token, "tagid": 123}
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/get",
            "params": {"access_token": self.token, "tagid": tagid},
        }
        r = self.send_api(req)
        # r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/tag/get", parm)
        return r.json()

    # 增加标签成员
    def add_tag_member(self, tagid,userid):
        """
         userlist只需要传入成员ID
        :param userid: 是成员ID
        :return:
        """
        req = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers",
            "params": {"access_token": self.token},
             "json": {"tagid": tagid,
                      "userlist":userid}
             }

        r = self.send_api(req)
        return r.json()

    # 删除标签成员
    def delete_tag_member(self, tagid,userid):
        """
         userlist只需要传入成员ID
         :param userid: 是成员ID
         :return:
        """
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers",
            "params": {"access_token": self.token},
            "json": {
                "tagid": tagid,
                "userlist": userid}
        }
        r = self.send_api(req)
        return r.json()

    # 获取标签列表
    def get_tag_list(self):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/list",
            "params": {"access_token": self.token}
        }
        r=self.send_api(req)
        return r.json()
