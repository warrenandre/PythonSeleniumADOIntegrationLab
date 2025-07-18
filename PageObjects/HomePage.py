from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class HomePage(BasePage):

    HEADER = (By.XPATH, '//*[contains(@class,"wp-block-site-title")]/a')
    SamplePageCLK = (By.XPATH, '//a[contains(text(),"Sample Page")]')
    # PROFILE_IMG = (By.CSS_SELECTOR,'[class*=header] img[alt="profile picture"]')

    def __int__(self,driver):
        super.__init__(driver)


    def get_header_value(self):
        """ Get home page header value """
        return self.get_element_text(self.HEADER)

    def is_sample_page_visible(self):
        """ Return sample page link is visible or not """
        return self.element_is_visible(self.SamplePageCLK)


