import pytest
from pages.auth_page_bycode import AuthPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


def test_invalid_login(web_browser):

    #Проверка недопустимости некорректного ввода

    page = AuthPage(web_browser)

    page.login.send_keys('123')

    page.getcode.click()

    assert WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/span')))

def test_valid_login(web_browser):

    #Проверка корректного ввода

    page = AuthPage(web_browser)

    page.login.send_keys('123@gmail.com')

    WebDriverWait(web_browser, 120).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, 'otp-form__timeout')))

    page.getcode.click()

    assert WebDriverWait(web_browser, 60).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'card-container__title'),
                                         "Код подтверждения отправлен"))

def test_standard_login(web_browser):

    #Проверка перехода к стандартному входу с паролем

    page = AuthPage(web_browser)

    page.auth_btn.click()

    assert WebDriverWait(web_browser, 60).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'card-container__title'),
                                         "Авторизация"))

def test_vk_login(web_browser):

    #Проверка перехода c помощью ВК

    page = AuthPage(web_browser)

    page.vk.click()

    assert WebDriverWait(web_browser, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'vkc__AuthRoot__contentIn'),  "Вход в «РТК Паспорт»"))

def test_ok_login(web_browser):

    #Проверка перехода c помощью ОК

    page = AuthPage(web_browser)

    page.ok.click()

    assert WebDriverWait(web_browser, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'ext-widget_h_tx'),  "Одноклассники"))

def test_mail_login(web_browser):

    #Проверка перехода c помощью mail

    page = AuthPage(web_browser)

    page.mail.click()

    assert WebDriverWait(web_browser, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'header__logo'),  "Мой Мир@Mail.Ru"))

def test_ya_login(web_browser):

    #Проверка перехода c помощью yandex

    page = AuthPage(web_browser)

    page.ya.click()
    page.ya.click()
    page.ya.wait_until_not_visible()

    assert WebDriverWait(web_browser, 30).until(
        EC.title_is("Авторизация"))

def test_logo(web_browser):

    #Проверка наличия логотипа и слогана

    page = AuthPage(web_browser)

    assert WebDriverWait(web_browser, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'what-is__title'),  "Личный кабинет"))

def test_help(web_browser):

    #Проверка перехода на страницу помощи

    page = AuthPage(web_browser)

    page.help.click()

    assert WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/div/div')))


