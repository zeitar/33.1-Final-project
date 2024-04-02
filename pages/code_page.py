from pages.base import WebPage
from pages.elements import WebElement


class CodePage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_smarthome&response_type=code&scope=openid&redirect_uri=https%3A%2F%2Flk.smarthome.rt.ru%2Foauth2%2Fcallback'
        super().__init__(web_driver, url)

    address = WebElement(id='address')
    getcode = WebElement(id='otp_get_code')
    auth_btn = WebElement(id='standard_auth_btn')
