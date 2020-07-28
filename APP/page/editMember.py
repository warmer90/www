from appium.webdriver.common.mobileby import MobileBy


from page.base import BasePage


class EditMember(BasePage):


    #删除成员
    def del_member(self):


        self._driver.find_element(MobileBy.XPATH,"//*[@text='删除成员']").click()
        self._driver.find_element(MobileBy.XPATH,"//*[@text='确定']").click()
        from APP.page.memberlist import MemberListPage
        return MemberListPage(self._driver)