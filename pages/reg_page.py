from pages.base import WebPage
from pages.elements import WebElement
from selenium.webdriver.common.by import By


class RegPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://client.rt.ru/registration'
        super().__init__(web_driver, url)

    name = WebElement(id='personal-data-rtk-input-0')

    email = WebElement(id='personal-data-rtk-input-1')

    phone = WebElement(id='personal-data-rtk-input-2')

    btn = WebElement(id='personal-data-rtk-button-0')

    cncl = WebElement(id='personal-data-rtk-button-1')

    policy = WebElement(xpath='/html/body/registration-user/div/div[2]/div/div[4]/span/a')

    phoneConf = WebElement(classname='modalContent')



