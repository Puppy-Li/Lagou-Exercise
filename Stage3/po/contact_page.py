from selenium.webdriver.common.by import By

from Stage3.po.add_member_page import AddMemberPage
from Stage3.po.base_page import BasePage


class ContactPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def goto_add_member(self):
        """
        go to add member page
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)

    def get_member_list(self):
        """
        get
        :return: return contact member list for assertion
        """
        ele = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth[2]")
        name_list = [i.text for i in ele]
        return [name_list]