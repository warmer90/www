import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebviewXueqiu:

    def setup(self):
        desire_caps = {
            "platformName": "Android",

            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            'chromedriverExecutable': 'D:\soft\appium-driver',
            "noReset": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click()

        print(self.driver.contexts)
        A_locator = (MobileBy.XPATH, "//android.view.View[@content-desc='A股开户']")
        #self.driver.switch_to.context(self.driver.contexts[-2])
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(A_locator))
        # 两种写法都可以定位到
        self.driver.find_element(*A_locator).click()
        time.sleep(5)

        # self.driver.find_element_by_accessibility_id('A股开户').click()
        kaihu_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(kaihu_window)
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element(MobileBy.ID, "phone-number").send_keys("17855221111")
        self.driver.find_element(MobileBy.ID, "code").send_keys("5546")
        self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="立即开户"]').click()
