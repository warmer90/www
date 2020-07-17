from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        desire_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "browserName": "Browser",
            "noReset": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)
        self.driver.find_element(By.ID, "index-kw").click()
        self.driver.find_element(By.ID, "index-kw").send_keys("appium")
        # 添加显示等待，等待元素加载出来
        search_locator = (By.ID, "index-bn")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).click()
