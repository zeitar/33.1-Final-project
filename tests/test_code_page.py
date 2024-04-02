import pytest
from pages.code_page import CodePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#\\\\\\\\\УМНЫЙ ДОМ/////////

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()

def test_invalid_login(web_browser):

    #Проверка недопустимости некорректного ввода

    page = CodePage(web_browser)

    page.address.send_keys('123')

    page.getcode.click()

    assert WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/span')))

def test_valid_login(web_browser):

    #Проверка корректного ввода

    page = CodePage(web_browser)

    page.address.send_keys('1111111111')

    page.getcode.click()

    assert WebDriverWait(web_browser, 60).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'card-container__title'),
                                         "Код подтверждения отправлен"))

def test_standard_login(web_browser):

    #Проверка перехода к стандартному входу с паролем

    page = CodePage(web_browser)

    page.auth_btn.click()

    assert WebDriverWait(web_browser, 60).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'card-container__title'),
                                         "Авторизация"))