from appium.webdriver.common.mobileby import MobileBy

from APP.page.personal_info import PersonalInfo
from page.base import BasePage


class MemberListPage(BasePage):


    # 点击添加成员
    def add_member(self):
        from APP.page.invitemember import InviteMember

        self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
                                                               'text("添加成员").instance(0));').click()

        return InviteMember(self._driver)

    #寻找成员
    def search_member(self,name):
        self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                                'scrollable(true).instance(0)).'
                                                                'scrollIntoView(new UiSelector().'
                                                                f'text("{name}").instance(0));').click()
        return PersonalInfo(self._driver)