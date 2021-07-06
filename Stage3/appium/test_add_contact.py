from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy


class TestAddContact:
    def setup(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        # desired_caps['automationName'] = 'uiautomator2'
        desired_caps['noReset'] = True
        desired_caps['skipServerInstallation'] = True
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('searchkey', [{'12345678901'},{'test'}])
    def test_add_contact(self, searchkey):
        """
        1. 打开微信应用
        2. 点击右上角 + 按钮
        3. 点击 ‘添加朋友’ 选项
        4. 点击搜索框，输入不存在的微信号或手机号
        5。 点击搜索
        6. 断言 搜索结果为 “该用户不存在”
        :return:
        """
        self.driver.find_element(MobileBy.ID, "com.tencent.mm:id/g_").click()
        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[contains(@text, '添加朋友')]").click()
        self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[contains(@text, '微信号/手机号')]").click()
        # 输入搜索内容
        self.driver.find_element(MobileBy.ID, "com.tencent.mm:id/ht").send_keys(searchkey)
        # 点击搜索
        self.driver.find_element(MobileBy.ID, "com.tencent.mm:id/kn").click()
        res = self.driver.find_element(MobileBy.ID, "com.tencent.mm:id/res").text
        assert "该用户不存在" in res


