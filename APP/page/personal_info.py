from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.mobile import Mobile

from APP.page.editMember import EditMember
from page.base import BasePage


class PersonalInfo(BasePage):
    def click_b(self):
        self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/h9p").click()
        self._driver.find_element(MobileBy.XPATH,"//*[@text='编辑成员']").click()

        return EditMember(self._driver)