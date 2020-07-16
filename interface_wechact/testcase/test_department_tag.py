import yaml

from interface_wechact.page.department import Department


class TestDepartmentTag:
    # token 只需要每个用例执行前执行一次就可以了，+_class 可以不用重复setup
    def setup_class(self):
        self.dep = Department()
        self.token = self.dep.get_token(self.dep.load("config.yaml")["corpsecret"])
        #"config.yaml"["corpsecret"])
    # 创建标签
    def test_create_tag(self):
        r = self.dep.create_tag("melo", 124)
        assert r["errcode"] == 0

    # 更新标签
    def test_update_tag(self):
        r = self.dep.update_tag("melo", 124)
        print(r)
        assert r["errcode"] == 0

    # 删除标签
    def test_delete_tag(self):
        r = self.dep.delete_tag(124)

        assert r["errcode"] == 0

    # 获取标签成员
    def test_get_member(self):
        r = self.dep.get_tag_member(12)
        print(r["userlist"])
        assert r["errcode"] == 0

    # 增加标签成员
    def test_add_tag_member(self):
        r = self.dep.add_tag_member(122,("CaoCao19","ANiu2"))
        print(r)
        assert r["errcode"] == 0

    # 删除标签成员
    def test_del_tag_member(self):
        r = self.dep.delete_tag_member(122,("CaoCao19","ANiu2"))
        print(r)
        assert r["errcode"] == 0

    # 获取标签列表
    def test_tag_list(self):
        r = self.dep.get_tag_list()
        print(r["taglist"])
        assert r["errcode"] == 0
