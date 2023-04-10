from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from webdriver_manager.chrome import ChromeDriverManager


class WrappedLocalWebDriver(Chrome):
    def __init__(self, chrome_options):
        super().__init__(chrome_options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
