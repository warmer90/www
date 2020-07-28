from appium.webdriver.common.mobileby import MobileBy

from page.base import BasePage


class InviteMember(BasePage):



    def click_memberadd(self):
        from APP.page.addmember import AddMember

        self._driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手动输入')]").click()

        return AddMember(self._driver)
