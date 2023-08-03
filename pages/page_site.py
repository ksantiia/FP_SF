from pages.base_page import WebPage
from pages.base_elements import WebElement


class Page(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth'
        super().__init__(web_driver, url)

    username = WebElement(id='username')

    email = WebElement(id='email')

    fog_pass = WebElement(id='forgot_password')

    password = WebElement(id='password')

    btn_logout = WebElement(id='logout_btn')

    firstName = WebElement(name='firstName')

    lastName = WebElement(name='lastName')

    address = WebElement(id='address')

    password_confirm = WebElement(id='password-confirm')

    btn = WebElement(css_selector='button[type="submit"]')

    mail_btn = WebElement(id='t-btn-tab-mail')

    login_btn = WebElement(id='t-btn-tab-login')

    ls_btn = WebElement(id='t-btn-tab-ls')

    register = WebElement(id='kc-register')

    new_pass = WebElement(id='t-btn-tab-ls')

    error = WebElement(id='form-error-message')

    error_two = WebElement(class_name='rt-input-container__meta')

    code_verif = WebElement(class_name='register-confirm-form-container__desc')
