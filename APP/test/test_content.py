import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestContent:
    def setup(self):
        desire_caps={
            "platformName":"Android",
            "deviceName":"warmer",
            "appPackage":"com.tencent.wework",
            "appActivity":".launch.LaunchSplashActivity",
            "noReset":True
        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        pass
    @pytest.mark.parametrize("user,gender,phonenum",
                             [
                             ("孙尚香", "女", "19933332223"),
                             ("秦香莲", "女", "19933332224"),
                             ("赵云1","男","19933332226"),])

    def test_contact(self,user,gender,phonenum):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().'
                                                       'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'手动输入')]").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/..//*[contains(@class,'EditText')]").send_keys(user)

       # gender='女'
        el=self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH,f"//*[@text='{gender}']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/f1e").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()
        el1=self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成功']").text
        assert el1=="添加成功"

