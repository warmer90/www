from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from APP.page.main import Main
from page.base import BasePage


class App(BasePage):

    def startapp(self):
        #如果_driver为空，创建driver，如果不为空复用driver
        if self._driver == None:
            desire_caps = {
                "platformName": "Android",
                "deviceName": "warmer",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": True
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        else:
            #launch_app()复用APP
            self.driver.launch_app()
        self.driver.implicitly_wait(20)
        return self

    def restartapp(self):
        pass

    def closeapp(self):
        pass

    #返回首页
    def main(self) -> Main:

        return Main(self.driver)
