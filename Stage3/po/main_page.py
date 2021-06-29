from selenium.webdriver.common.by import By

from Stage3.po.add_member_page import AddMemberPage
from Stage3.po.base_page import BasePage
from Stage3.po.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_contact(self):
        """
        go to contact page
        :return:
        """
        return ContactPage()

    def goto_add_member(self):
        """
        go to add member page
        :return:
        """
        self.driver.find_element((By.CSS_SELECTOR, ".ww_indexImg_AddMember")).click()
        return AddMemberPage()