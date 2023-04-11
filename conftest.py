import pytest
from selenium import webdriver

from helpers.wrapp_driver import WrappedLocalWebDriver


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--start-maximized')
    options.add_argument("--auto-open-devtools-for-tabs")

    browser = WrappedLocalWebDriver(chrome_options=options)
    browser.implicitly_wait(20)
    browser.maximize_window()
    yield browser
    browser.quit()
