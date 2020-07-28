from appium.webdriver.common.mobileby import MobileBy

from APP.page.memberlist import MemberListPage
from page.base import BasePage


class Main(BasePage):

    def goto_message(self):
        pass

    # 进入通讯录
    def goto_address(self):

        self._driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()

        return MemberListPage(self._driver)

    def gotoworkbench(self):
        pass

    def goto_myself(self):
        pass
