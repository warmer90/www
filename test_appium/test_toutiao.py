from appium import webdriver


class TestWebviewXueqiu:

    def setup(self):
        desire_caps = {
            "platformName": "Android",
            #"uid": "91QEBNH23GC6",
            "deviceName":"91QEBNH23GC6",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.MainActivity",
            #'chromedriverExecutable': 'D:\soft\appium-driver',
            "noReset": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_webview(self):
        pass