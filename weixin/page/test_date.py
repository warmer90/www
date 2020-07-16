import time

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDate:
    def setup(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        self.driver.implicitly_wait(3)

    @pytest.mark.parametrize("username1,myid,phonenum", [("aaaa", "324241", "16633231111")])

    #@pytest.mark.parametrize("username1,myid,phonenum", yaml.safe_load(open("./data.yaml")))
    def test_add_member(self, username1, myid, phonenum):

        print(username1)
        #self.driver.find_element(By.CSS_SELECTOR, ".js_add_member").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "username").send_keys(username1)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(myid)
        self.driver.find_element(By.CSS_SELECTOR, ".ww_telInput_mainNumber").send_keys(phonenum)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()