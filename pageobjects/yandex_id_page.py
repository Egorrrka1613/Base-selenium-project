import allure
from selenium.webdriver.common.by import By

from pageobjects.base_page import BasePage, get_element_by_xpath


def get_iframe_by_css(class_name):
    return By.CSS_SELECTOR, f"iframe.{class_name}"


class YandexIdPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.url = 'https://id.yandex.ru/'

    @allure.step('Получить логин пользователя')
    def get_current_user_login(self) -> str:
        self.click_element('Link UserID-Account')

        iframe = self.check_element(get_iframe_by_css("UserWidget-Iframe"))
        self.driver.switch_to.frame(iframe)

        xpath = get_element_by_xpath(attribute_name='Text Text_typography_secondary UserId-SecondLine Subname')
        login = self.check_element(xpath).text
        return login

    @allure.step('Клик по элементу: "{attribute_name}"')
    def click_element(self, attribute_name):
        el = self.check_element(get_element_by_xpath(attribute_name))
        el.click()
        return self
