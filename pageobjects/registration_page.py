from urllib.parse import urljoin

from pageobjects.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.page_url = urljoin(self.url, "/registration")
