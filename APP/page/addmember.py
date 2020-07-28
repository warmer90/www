from appium.webdriver.common.mobileby import MobileBy
from APP.page.invitemember import InviteMember
from page.base import BasePage


class AddMember(BasePage):



    def set_name(self, user):
        self._driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/..//*[contains(@class,'EditText')]").send_keys(user)
        return self

    def set_gender(self, gender):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self._driver.find_element(MobileBy.XPATH, f"//*[@text='{gender}']").click()
        return self

    def set_phonenum(self, phonenum):
        self._driver.find_element(MobileBy.ID, "com.tencent.wework:id/f1e").send_keys(phonenum)

        return self

    def chick_save(self):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        el1 = self._driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").text

        return InviteMember(self._driver)
