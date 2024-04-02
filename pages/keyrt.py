from pages.base import WebPage
from pages.elements import WebElement


class KeyPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://key.rt.ru/'
        super().__init__(web_driver, url)

    cab = WebElement(xpath='/html/body/section/div/div[2]/a[1]')
    address = WebElement(id='address')
    getcode = WebElement(id='otp_get_code')
    auth_btn = WebElement(id='standard_auth_btn')