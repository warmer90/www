import time

import pytest
import yaml
from selenium.webdriver.common.by import By

from weixin.page.base_page import BasePage
from weixin.page.contact import Contact


class AddMember(BasePage):

    # def setup(self):
    #     self.driver=webdriver.Chrome()
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    #     self.driver.implicitly_wait(10)

    # @pytest.mark.parametrize("a,b,c", [("aaaa", "vvvv","16633231111")])
    # def test_date(self, a, b):
    #     print(a)
    #     # print(b)
    #
    """
    @pytest.mark.parametrize("a,b,c", [("aaaa", "324241", "16633231111")])
    #@pytest.mark.parametrize("username1",[("aaaa")])
    #@pytest.mark.parametrize("username1,myid,phonenum", yaml.safe_load(open("./data.yaml")))
    def add_member(self, a,b,c):
        print(a)
        time.sleep(2)

        self.find(By.ID, "username").send_keys(a)
        self.find(By.ID,"memberAdd_acctid").send_keys("22145")
        self.find(By.CSS_SELECTOR,".ww_telInput_mainNumber").send_keys("12455558888")
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        return Contact(self.driver)

    """
    print("****33333-----")


    def add_member(self):
        print("*********-------")


        self.driver.find_element_by_id("username").send_keys("bear5")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("5522215")
        self.driver.find_element_by_css_selector(".ww_telInput_mainNumber").send_keys("15545253234")
        self.driver.find_element_by_css_selector(".js_btn_save").click()
        time.sleep(2)
        return Contact(self.driver)

