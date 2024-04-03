import pytest
from pages.keyrt import KeyPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


#\\\\\\\\\Ключ/////////


def test_invalid_login(web_browser):

    #Проверка недопустимости некорректного ввода

    page = KeyPage(web_browser)
    page.cab.click()

    page.address.send_keys('123')

    page.getcode.click()

    assert WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/span')))

def test_valid_login(web_browser):

    #Проверка корректного ввода почты

    page = KeyPage(web_browser)
    page.cab.click()

    page.address.send_keys('123@gmail.com')

    WebDriverWait(web_browser, 120).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, 'otp-form__timeout')))

    page.getcode.click()

    assert WebDriverWait(web_browser, 60).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'card-container__title'),
                                         "Код подтверждения отправлен"))

def test_standard_login(web_browser):

    #Проверка перехода к стандартному входу с паролем

    page = KeyPage(web_browser)
    page.cab.click()

    page.auth_btn.click()

    assert WebDriverWait(web_browser, 60).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'card-container__title'),
                                         "Авторизация"))