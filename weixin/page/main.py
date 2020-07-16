import time

from selenium.webdriver.common.by import By

from weixin.page.addMember import AddMember
from weixin.page.base_page import BasePage
from weixin.page.deparment import Deparment


class Main(BasePage):




    def goto_add_member(self):

        self.find(By.CSS_SELECTOR,".ww_indexImg_AddMember").click()

        time.sleep(2)
        return AddMember(self.driver)

    def goto_add_dep(self):

        self.find(By.CSS_SELECTOR,".frame_nav_item_title").click()
        return Deparment(self.driver)