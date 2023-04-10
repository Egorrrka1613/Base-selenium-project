import os
import time
from abc import ABC, abstractmethod

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def get_input_by_css(input_id):
    return By.CSS_SELECTOR, f"input#{input_id}"


def get_button_by_css(button_id):
    return By.CSS_SELECTOR, f"button#{button_id}"


def get_a_by_css(a_id):
    return By.CSS_SELECTOR, f"a#{a_id}"


def get_element_by_xpath(attribute_name, attribute_type='class', element_type='*'):
    return By.XPATH, f"//{element_type}[@{attribute_type}='{attribute_name}']"


class BasePage(ABC):
    __wait_time_in_second = int(os.environ["EXPLICITLY_WAIT_IN_SECOND"])

    @abstractmethod
    def __init__(self, driver) -> None:
        self.driver = driver
        self.url = os.environ["BASE_URL"]

    def go_to(self):
        with allure.step(f'Открыть страницу по адресу "{self.url}"'):
            self.driver.get(self.url)
            return self

    @allure.step('Ождание загрузки страницы в "{timeout} секунд"')
    def wait_page_is_load(self, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script('return document.readyState') == 'complete'
            )
        except TimeoutException:
            print(f"Страница грузится дольше чем {timeout} cекунд")

    @allure.step('Поиск элемента по локатору: "{locator}"')
    def check_element(self, locator, timeout=__wait_time_in_second):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator) and
                             EC.visibility_of_element_located(locator),
                             message=f"Элемент {locator} не найден в течении {timeout} секунд")
        return element

    def get_input_element(self, input_id):
        return self.check_element(get_input_by_css(input_id))

    @allure.step('Ввод текста "{text}" в поле "{field_name}"')
    def send_text_to_input(self, field_name, text):
        el = self.get_input_element(field_name)
        el.send_keys(u'\ue009' + u'\ue003')
        el.send_keys(text)
        time.sleep(0.1)
        return self

    @allure.step('Клик по кнопке: "{button_id}"')
    def click_button(self, button_id, timeout=__wait_time_in_second):
        self.check_element(get_button_by_css(button_id), timeout).click()
        return self

    @allure.step('Клик по гиперссылке: "{a_id}"')
    def click_a(self, a_id, timeout=__wait_time_in_second):
        self.check_element(get_a_by_css(a_id), timeout).click()
        return self

    @allure.step('Получить признак наличия на странице элемента с локатором "{locator}"')
    def is_exists_element(self, locator):
        return len(self.driver.find_elements(*locator)) > 0
