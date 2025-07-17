from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest
import os
from datetime import datetime
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from PageObjects.SeleniumScreenRecorder import SeleniumScreenRecorder

@pytest.fixture()
def setup(browser):

    global driver

    if browser == 'chrome':

        chrome_option = webdriver.ChromeOptions()
        chrome_option.set_capability("browserName", "chrome")
        chrome_option.add_argument('--incognito')
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_option)
        driver.maximize_window()

    elif browser == 'firefox':
        firefox_option = Options()
        firefox_option.set_capability("browserName", "firefox")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_option)

    else:
        chrome_option = webdriver.ChromeOptions()
        chrome_option.set_capability("browserName", "chrome")
        chrome_option.add_argument('--incognito')
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_option)
        driver.maximize_window()

    yield driver
    driver.close()

@pytest.fixture()
def screen_recorder(setup):
    """Screen recorder fixture"""
    driver = setup
    recorder = SeleniumScreenRecorder(driver)
    yield recorder


def pytest_addoption(parser):  # this will get value from CLI hooks
    parser.addoption('--browsername')


@pytest.fixture()
def browser(request):   # this will return browser value to setup method
    return request.config.getoption('--browsername')

