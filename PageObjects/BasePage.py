from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ConfigData.config import TestData


class BasePage:

    """The BasePage class holds all common functionality across the website."""

    def __init__(self, driver):
        """ This function is called every time a new object of the base class is created"""
        self.driver = driver
        self.driver.get(TestData.baseURL)

    def do_click(self, by_locator):
        """ Performs click on web element """
        WebDriverWait(self.driver, TestData.shortwait).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        """ Performs send kyes to web element """
        WebDriverWait(self.driver, TestData.shortwait).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        """ Get element text """
        element = WebDriverWait(self.driver, TestData.shortwait).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def element_is_enable(self, by_locator):
        """ Return element is enable or not """
        element = WebDriverWait(self.driver, TestData.shortwait).until(EC.visibility_of_element_located(by_locator))
        return bool(element.is_enabled())

    def element_is_visible(self, by_locator):
        """ Return element is visible or not """
        #add try catch
        try:
            element = WebDriverWait(self.driver, TestData.shortwait).until(EC.visibility_of_element_located(by_locator))
            return bool(element.is_displayed())
        except TimeoutError:
            print(f"Element not found: {by_locator}")
            return False
        except:
            return False

    def get_title(self, title):
        """Returns the title of the page"""
        WebDriverWait(self.driver, TestData.shortwait).until(EC.title_is(title))
        return self.driver.title
