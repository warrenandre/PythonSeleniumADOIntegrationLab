from selenium.webdriver.common.by import By

from ConfigData.config import TestData
from PageObjects.BaseLoginPage import BaseLoginPage
from PageObjects.HomePage import HomePage


class LoginPage(BaseLoginPage):
    txt_USERNAME = (By.XPATH, '//input[@name="log"]')
    txt_PASSWORD = (By.XPATH, '//input[@name="pwd"]')
    btn_LOGIN = (By.XPATH, '//input[@type="submit"]')
    lnk_Edit_Site = (By.XPATH, '//*[contains(@id,"wp-admin-bar-my-sites")]/a')
    # screen_recorderr = screen_recorder
    def __init__(self, driver):
        super().__init__(driver)

    def verify_title(self, title):
        """ Get title """
        return self.get_title(title)

    def login(self, username, password,screen_recorder):
        """ Login """
        self.do_send_keys(self.txt_USERNAME, username)  # set username
        self.do_send_keys(self.txt_PASSWORD, password)  # set password
        screen_recorder.capture_screenshot("login")
        self.do_click(self.btn_LOGIN)
        screen_recorder.capture_screenshot("afterlogin")
        return HomePage(self.driver)

    def is_edit_site_available(self):
        """ Return forgot link is visible or not """
        return self.get_element_text(self.lnk_Edit_Site)