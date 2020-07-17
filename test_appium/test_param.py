import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to


class TestParams:
    def setup(self):
        desire_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            "noReset": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()

    @pytest.mark.parametrize("usname,type1,expect_price", [("xiaomi", "01810", 15), ("alibaba", "BABA", 240)])
    def test_search(self, usname, type1, expect_price):
        """
        1.打开雪球
        2. 点击搜索框
        3. 输入 搜索词 ‘alibaba' or ’xiaomi' ...
        4. 点击第一个搜索结果
        5  判断 股票价格
        :return:
        """
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(f"{usname}")
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        currenc_price = float(self.driver.find_element_by_xpath(
            f"//*[@text='{type1}'] /../../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)

        print((currenc_price))
        print(type(expect_price))
        assert_that(currenc_price, close_to(expect_price, currenc_price * 1.1))
