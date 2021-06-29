from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    """
    BasePage提供公共方法的封装，即与页面逻辑无关的封装
    """
    _base_url = ""
    def __init__(self, base_driver=None):
        if base_driver is None:
            # 通过remote复用浏览器操作
            chrome_arg = webdriver.ChromeOptions()
            # 加入调试地址
            chrome_arg.debugger_address = '127.0.0.1:9222'
            # 实例化driver对象
            self.driver = webdriver.Chrome(options=chrome_arg)
            # 打开首页
            #self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.get(self.base_url)
            # 添加隐式等待，解决no such element问题
            self.driver.implicitly_wait(3)
        else:
            # 将self.driver添加一个WebDriver对象注解，解决类型提示的问题
            # 注解本身没有任何的赋值作用，方便IDE操作
            self.driver: WebDriver = base_driver

    def find(self, by, locator=None):
        # 如果只传入一个元组参数
        if locator is None:
            return self.driver.find_element(*by)
        # 适配多种传参情景
        else:
            return self.driver.find_element(by=by, value=locator)