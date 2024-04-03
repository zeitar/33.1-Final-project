import pytest
from pages.reg_page import RegPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


def test_invalid_name1(web_browser):

    #Проверка недопустимости некорректного имени

    page = RegPage(web_browser)

    page.name.send_keys('123')

    page.email.send_keys("123@gmail.com")

    page.phone.send_keys("111111111")

    page.btn.click()

    assert WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/registration-user/div/div[2]/div/div[2]/div[1]/span')))

def test_invalid_name2(web_browser):

    #Проверка недопустимости двух заглавных букв подряд

    page = RegPage(web_browser)

    page.name.send_keys('ИИванов Иван Иванович')

    page.email.send_keys("123@gmail.com")

    page.phone.send_keys("111111111")

    page.btn.click()

    assert WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/registration-user/div/div[2]/div/div[2]/div[1]/span')))

def test_invalid_name3(web_browser):

    #Проверка недопустимости более двух одиннаковых символов подряд в ФИО

    page = RegPage(web_browser)

    page.name.send_keys('Иванооов Иван Иванович')

    page.email.send_keys("123@gmail.com")

    page.phone.send_keys("111111111")

    page.btn.click()

    assert WebDriverWait(web_browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/registration-user/div/div[2]/div/div[2]/div[1]/span')))

def test_invalid_mail(web_browser):

    #Проверка недопустимости некорректной почты

    page = RegPage(web_browser)

    page.name.send_keys('Иванов Иван Иванович')

    page.email.send_keys("123")

    page.phone.send_keys("111111111")

    page.btn.click()

    assert page.get_current_url() == 'https://client.rt.ru/registration'

def test_invalid_phone1(web_browser):

    #Проверка недопустимости некорректного номера меньше 12 цифр

    page = RegPage(web_browser)

    page.name.send_keys('Иванов Иван Иванович')

    page.email.send_keys("123@gmail.com")

    page.phone.send_keys("123")

    page.btn.click()

    assert page.get_current_url() == 'https://client.rt.ru/registration'

def test_valid_input(web_browser):

    #Проверка ввода допустимых значений

    page = RegPage(web_browser)

    page.name.send_keys('Иванов Иван Иванович')

    page.email.send_keys("123@gmail.com")

    page.phone.send_keys("111111111")

    page.btn.click()

    assert WebDriverWait(web_browser, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'registration-user__personalData__title'), "Код подтверждения отправлен"))

def test_invalid_phone(web_browser):

    #Отмена регистрации

    page = RegPage(web_browser)

    page.cncl.click()

    assert page.get_current_url() == 'https://passport.rt.ru/auth/realms/b2b/protocol/openid-connect/auth?client_id=lk_b2b&redirect_uri=http%3A%2F%2Fclient.rt.ru&state=ffffff%3A0000%3A111111&response_type=code&scope=openid'

