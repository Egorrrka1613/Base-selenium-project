import random
from urllib.parse import urljoin

import allure

from pageobjects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.page_url = urljoin(self.url, "/auth")

    @allure.step('Авторизация по логину "{login}" и паролю "{password}"')
    def auth_by_login_pass(self, login, password):
        self.send_text_to_input('passp-field-login', login)
        self.click_button('passp\:sign-in')
        self.send_text_to_input('passp-field-passwd', password)
        self.click_button('passp\:sign-in')
        self.wait_page_is_load(5)

    @allure.step('Ввести случайный пароль 5 раз')
    def broot_force_password(self):
        for attempt in range(6):
            self.send_text_to_input('passp-field-passwd', random.randint(100000000, 9999999999999999))
            self.click_button('passp\:sign-in')
