import json

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver1=None):
        if driver1 == None:
            option=Options()
            option.debugger_address="localhost:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        else:
            self.driver = driver1

        self.driver.implicitly_wait(5)


    def find(self,by,value):
        return self.driver.find_element(by,value)

    def finds(self, by, value):
        return self.driver.find_elements(by, value)

        # def save_cookie(self):
        # cookies = self.driver.get_cookies()
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)

        # cookie = self.driver.get_cookies()
        # with open("cookie.json", "w") as f:
        #     json.dump(obj=cookie, fp=f)

    def get_cookie(self):
        with open("cookie.json", "rb") as f:
            cookies = json.load(f)

        for cookie in cookies:
            # if "false" in cookies:
            #    cookie.replace("False")
            print(cookie)
            self.driver.add_cookie(cookie)
        return self.driver
