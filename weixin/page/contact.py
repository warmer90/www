import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from weixin.page.base_page import BasePage


class Contact(BasePage):

    def get_member(self):
        print(11111111)
        list_all = []
        while True:
            #ele=(By.CSS_SELECTOR, ".ww_pageNav_info_text")
           # WebDriverWait.until(expected_conditions.staleness_of)
            # 获取翻页。message获取到的是 1/3
            #message: str = self.driver.find_element(By.CSS_SELECTOR, ".ww_pageNav_info").text
            message: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text


            print("3322252111",message)
            print(222222)
            # 得到当前页，和总页数
            cur_page, total_page = [i for i in message.split("/", 1)]
            print(3333333333)
            member_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            print(total_page)
            print(cur_page)
            # 拿出所有成员
            for ele in member_list:
                list_all.append(ele.get_attribute("title"))

            if cur_page == total_page:
                print(list_all)
                return list_all

            print(list_all)
            self.find(By.CSS_SELECTOR, ".js_next_page").click()

    def add_member(self):
        return Contact()
