from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?response_type=code&scope=openid&client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk-api.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Flk.rt.ru%252F&state=%7B%22uuid%22%3A%22C680C3FA-E793-40E4-A6EC-D752AC4C508B%22%7D'
        super().__init__(web_driver, url)

    #email or phone number
    login = WebElement(id='address')

    getcode = WebElement(id='otp_get_code')

    auth_btn = WebElement(id='standard_auth_btn')

    agr = WebElement(id='rt-auth-agreement-link')

    vk = WebElement(id='oidc_vk')

    ok = WebElement(id='oidc_ok')

    mail = WebElement(id='oidc_mail')

    ya = WebElement(id='oidc_ya')

    help = WebElement(id='faq-open')

    policy = WebElement(id='rt-auth-agreement-link')