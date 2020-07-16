from selenium.webdriver.common.by import By

from weixin.page.base_page import BasePage


class Deparment(BasePage):

    def add_dep(self):
        self.find(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click

