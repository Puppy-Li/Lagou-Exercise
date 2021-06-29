from selenium.webdriver.common.by import By

from Stage3.po.base_page import BasePage


class AddMemberPage(BasePage):
    _username_ele = (By.ID, "username")

    def add_member(self, name):
        """
        add member
        :return: return instance in contact page
        """
        # import within function avoid of loop import issue
        from Stage3.po.contact_page import ContactPage
        self.find(*self._username_ele).send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys("110")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13155557777")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()

        return ContactPage()

    def add_member_fail(self, name):
        from Stage3.po.contact_page import ContactPage
        # 解包元组，传入两个参数
        self.driver.find_element(*self._username_ele).send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("110")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13155557777")
