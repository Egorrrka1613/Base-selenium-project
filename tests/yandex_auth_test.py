import os
import random

from pageobjects.base_page import get_element_by_xpath
from pageobjects.login_page import LoginPage
from pageobjects.registration_page import RegistrationPage
from pageobjects.yandex_id_page import YandexIdPage


def test_login(browser):
    login, password = os.environ["LOGIN"], os.environ["PASSWORD"]

    page = LoginPage(browser).go_to()
    page.auth_by_login_pass(login, password)
    page = YandexIdPage(browser)

    assert page.is_exists_element(
        get_element_by_xpath('ID-SearchField-Control')), 'Элемент личного кабинета не найден. Авторизация не успешна'
    assert browser.current_url == page.url, 'Не был выполнен переход на домен "id.yandex.ru"'
    assert login == page.get_current_user_login(), f'Фактический логин: {page.get_current_user_login()} ' \
                                                   f'не совпадает с ожидаемым: {login}'


def test_login_by_block_user(browser):
    login, password = os.environ["BLOCKED_LOGIN"], os.environ["PASSWORD"]

    page = LoginPage(browser).go_to()
    page.auth_by_login_pass(login, password)

    assert page.is_exists_element(
        get_element_by_xpath('field:input-passwd:hint', 'id')), 'Элемент с текстом контроля не найден'

    element_text = page.check_element(get_element_by_xpath('field:input-passwd:hint', 'id')).text
    assert element_text == 'Неверный пароль', f'Текст контроля не соответсвует.' \
                                              f'Ожидался текст "Неверный пароль" ' \
                                              f'Фактически отображается "{element_text}"'


def test_login_by_incorrect_password(browser):
    login, password = os.environ["LOGIN"], os.environ["PASSWORD"] + '1'

    page = LoginPage(browser).go_to()
    page.auth_by_login_pass(login, password)

    assert page.is_exists_element(
        get_element_by_xpath('field:input-passwd:hint', 'id')), 'Элемент с текстом контроля не найден'

    element_text = page.check_element(get_element_by_xpath('field:input-passwd:hint', 'id')).text
    assert element_text == 'Неверный пароль', f'Текст контроля не соответсвует.' \
                                              f'Ожидался текст "Неверный пароль" ' \
                                              f'Фактически отображается "{element_text}"'


def test_redirect_to_registration(browser):
    page = LoginPage(browser).go_to()
    page.click_a('passp\:exp-register')
    page = RegistrationPage(browser)

    assert page.is_exists_element(
        get_element_by_xpath('registration__block', 'class')), 'Таблица регистрации отсуствует на странице'
    assert page.url in browser.current_url, f'Не был выполнен переход на домен "{page.url}". ' \
                                            f'Текущий адрес "{browser.current_url}"'


def test_broot_force_login(browser):
    login = os.environ['LOGIN_BY_BROOT_FORCE']
    password = random.randint(100000000, 9999999999999999)

    page = LoginPage(browser).go_to()
    page.auth_by_login_pass(login, password)
    page.broot_force_password()
    assert page.is_exists_element(
        get_element_by_xpath('AuthPasswordForm-captcha', 'class')), 'Окно ввода капчи отсутствует на странице'
