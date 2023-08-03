import pytest
import time
from selenium.webdriver.common.by import By
from pages.page_site import Page
from setting import valid_password, valid_email, valid_phone, valid_login, valid_firstname, valid_lastname, valid_ls, lat_lastname, lat_firstname

# Для запуска тестов, возможно понадобится использование капчи.
# Добавте ее в тест при необходимости для ввода кода вручную.
# try:
#     if driver.find_element(By.CLASS_NAME, 'rt-captcha__image'):
#         time.sleep(20)
# except BaseException:
#     pass


# Тест на форму регистрации на сайте.
# Данный тест реализован только до запроса кода-подтверждения, так как при успешном заполнении формы данное значение
# нужно вводить вручную.
@pytest.mark.parametrize('firstName, lastName, address, password, password_confirm, test_type ',
                         [(valid_firstname, valid_lastname, valid_email, valid_password, valid_password, 'positive'),
                          ('', '', '', '', '', 'negative'),
                          (valid_firstname, valid_lastname, valid_email, 'ugkugkgkg', 'ugkugkgkg', 'negative'),
                          (valid_firstname, valid_lastname, 'yjfjfhjvj.ru', valid_password, valid_password, 'negative'),
                          (valid_firstname, valid_lastname, valid_email, valid_password, 'Gjggchgchjfg7', 'negative'),
                          (lat_firstname, lat_lastname, valid_phone, valid_password, valid_password, 'negative')
                          ])
def test_register(driver, firstName, lastName, address, password, password_confirm, test_type):

    page = Page(driver)

    page.register.click()

    # Получаем адрес текущей страницы.
    first_page = page.get_current_url()

    # Вводим данные
    page.firstName.send_keys(firstName)
    page.lastName.send_keys(lastName)
    page.address.send_keys(address)
    page.password.send_keys(password)
    page.password_confirm.send_keys(password_confirm)
    # Нажимаем на кнопку регистрации
    page.btn.click()

    # Получаем адрес текущей страницы.
    second_page = page.get_current_url()

    if test_type == 'positive':
        code = page.code_verif
        assert 'Kод подтверждения отправлен на адрес' in code.get_text() # Проверяем, что находимся на странице
                                                                        # для введения кода из сообщения.
        assert first_page != second_page  # Проверяем, что стартовая страница не равна ссылке после входа в аккаунт.
    else:
        if firstName == '' and lastName == '' and address == '' and password == '' and password_confirm == '':
            assert first_page == second_page   # Проверяем, что после нажания кнопки регистрации, адрес страницы не изменился
        elif firstName == lat_firstname or lastName == lat_lastname:
            err_str = page.error_two
            assert err_str.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' # Проверяем, что система выдает
                                                                                                    # ошибку при введении имении и фамилии латиницей.
        elif password != password_confirm:
            err_str = page.error_two
            assert err_str.get_text() == 'Пароли не совпадают'   # Проверяем, что система выдает ошибку, если пароли разные
        elif '@' not in address:
            err_str = page.error_two  # Проверяем, то система выдает ошибку, если эл. почта или телефон введены не корректно
            assert err_str.get_text() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
        else:
            err_str = page.error_two
            assert 'Пароль должен содержать' in err_str.get_text() # Проверяем, что система выдает ошибку,
                                                                    # если формат пароля введен не корректно


# Тест на возможность входа в личный кабинет по средствам эл. почты.
# Параметр test_type передаем для разделения тестов на позитивные и негативные.
@pytest.mark.parametrize('username, password, test_type',
                         [(valid_email, valid_password, 'positive'),
                          ('', '', 'negative'),
                          ('yjfjf@hjvj.ru', valid_password, 'negative'),
                          (valid_email, 'gjggchgchjfg7', 'negative'),
                          ])
def test_enter_mail(driver, username, password, test_type):

    page = Page(driver)

    page.mail_btn.click()

    # получаем адрес стартовой страницы.
    start_page = page.get_current_url()

    # Вводим данные.
    page.username.send_keys(username)
    page.password.send_keys(password)

    # Входим в аккаунт.
    page.btn.click()

    # Получаем адрес страницы входа в аккаунт.
    second_page = page.get_current_url()

    if test_type == 'positive':
        assert 'https://b2c.passport.rt.ru/account_b2c/' in page.get_current_url()  # Проверяем содержиться ли ссылка на личный кабинет в полученной ссылке, после входа
        assert start_page != second_page  # Проверяем, что стартовая страница не равна ссылке после входа в аккаунт.
    else:
        if username == '' and password == '':
            assert start_page == second_page   # Проверяем, что после нажания кнопки "Вход", адрес страницы не изменился
        else:
            err_msg = page.error
            assert err_msg.get_text() == "Неверный логин или пароль"  # Проверяем, что на странице появилось высветилось соответствующее сообщение.


# Тест на возможность входа в личный кабинет по средствам Логина.
# Параметр test_type передаем для разделения тестов на позитивные и негативные.
@pytest.mark.parametrize('username, password, test_type',
                         [(valid_login, valid_password, 'positive'),
                          ('', '', 'negative'),
                          ('Аlina', valid_password, 'negative'),
                          (valid_login, 'gjggchgchjfg7', 'negative'),
                          ('747557', valid_password, 'negative')
                          ])
def test_enter_login(driver, username, password, test_type):

    page = Page(driver)

    page.login_btn.click()

    # получаем адрес стартовой страницы.
    start_page = page.get_current_url()

    # Вводим данные.
    page.username.send_keys(username)
    page.password.send_keys(password)

    # Входим в аккаунт.
    page.btn.click()

    # Получаем адрес страницы входа в аккаунт.
    second_page = page.get_current_url()

    if test_type == 'positive':
        assert 'https://b2c.passport.rt.ru/account_b2c/' in page.get_current_url()  # Проверяем содержиться ли ссылка на личный кабинет в полученной ссылке, после входа
        assert start_page != second_page  # Проверяем, что стартовая страница не равна ссылке после входа в аккаунт.
    else:
        if username == '' and password == '':
            assert start_page == second_page  # Проверяем, что после нажания кнопки "Вход", адрес страницы не изменился
        else:
            err_msg = page.error
            assert err_msg.get_text() == "Неверный логин или пароль"  # Проверяем, что на странице появилось высветилось соответствующее сообщение.


# Тест на возможность входа в личный кабинет по средствам номера телефона.
# Параметр test_type передаем для разделения тестов на позитивные и негативные.
@pytest.mark.parametrize('username, password, test_type',
                         [(valid_phone, valid_password, 'positive'),
                          ('', '', 'negative'),
                          ('+79194737790', valid_password, 'negative'),
                          (valid_phone, 'gjggchgchjfg7', 'negative')
                          ])
def test_enter_phone(driver, username, password, test_type):

    page = Page(driver)

    # получаем адрес стартовой страницы.
    start_page = page.get_current_url()

    # Вводим данные.
    page.username.send_keys(username)
    page.password.send_keys(password)

    # Входим в аккаунт.
    page.btn.click()

    # Получаем адрес страницы входа в аккаунт.
    second_page = page.get_current_url()

    if test_type == 'positive':
        assert 'https://b2c.passport.rt.ru/account_b2c/' in page.get_current_url()  # Проверяем содержиться ли ссылка на личный кабинет в полученной ссылке, после входа
        assert start_page != second_page  # Проверяем, что стартовая страница не равна ссылке после входа в аккаунт.
    else:
        if username == '' and password == '':
            assert start_page == second_page  # Проверяем, что после нажания кнопки "Вход", адрес страницы не изменился
        else:
            err_msg = page.error
            assert err_msg.get_text() == "Неверный логин или пароль"  # Проверяем, что на странице появилось высветилось соответствующее сообщение.


# Тест на возможность входа в личный кабинет по средствам лицевого счета.
# Параметр test_type передаем для разделения тестов на позитивные и негативные.
@pytest.mark.parametrize('username, password, test_type',
                         [(valid_ls, valid_password, 'positive'),
                          (0, '', 'negative'),
                          ('456678990986', valid_password, 'negative'),
                          (valid_ls, 'gjggchgchjfg7', 'negative')
                          ])
def test_enter_ls(driver, username, password, test_type):
    page = Page(driver)

    page.ls_btn.click()

    # получаем адрес стартовой страницы.
    start_page = page.get_current_url()

    # Вводим данные.
    page.username.send_keys(username)
    page.password.send_keys(password)

    # Входим в аккаунт.
    page.btn.click()

    # Получаем адрес страницы входа в аккаунт.
    second_page = page.get_current_url()

    if test_type == 'positive':
        assert 'https://b2c.passport.rt.ru/account_b2c/' in page.get_current_url()  # Проверяем содержиться ли ссылка на личный кабинет в полученной ссылке, после входа
        assert start_page != second_page  # Проверяем, что стартовая страница не равна ссылке после входа в аккаунт.
    else:
        if username == '' and password == '':
            assert start_page == second_page  # Проверяем, что после нажания кнопки "Вход", адрес страницы не изменился
        else:
            err_msg = page.error
            assert err_msg.get_text() == "Неверный логин или пароль"  # Проверяем, что на странице появилось высветилось соответствующее сообщение.


# Тест на востановление пароля по средствам эл. почты.
# Реализованны только негативные тесты, где для востановления пароля используется не существующий адрес электронной почты.
@pytest.mark.parametrize('username, password, username_rep',
                         [(valid_email, 'AKfbvzdufvu95v', '857459880'),
                          (valid_email, 'AKfbvzdufvu95v', ''),
                          (valid_email, 'AKfbvzdufvu95v', 'yjfjf@hjvj.ru')
                          ])
def test_new_password_email(driver, username, password, username_rep):

    page = Page(driver)

    page.mail_btn.click()

    # Вводим данные.
    page.username.send_keys(username)
    page.password.send_keys(password)

    # Входим в аккаунт.
    page.btn.click()
    # Переходим к востановлению пароля.
    page.fog_pass.click()

    page_first = page.get_current_url()

    # Вводим почту для востановления аккаунта
    page.username.send_keys(username_rep)

    page.btn.click()

    sec_page = page.get_current_url()

    if username_rep == '':
        assert page_first == sec_page  # Проверяем, что после нажания кнопки "Вход", адрес страницы не изменился
    else:
        err_msg = page.error
        assert err_msg.get_text() == "Неверный логин или текст с картинки"  # Проверяем, что на странице появилось высветилось соответствующее сообщение.


# Тест на востановление пароля по средствам номера телефона.
# Реализованны только негативные тесты, где для востановления пароля используется не существующий номер телефона.
@pytest.mark.parametrize('username, password, username_rep',
                         [(valid_phone, 'AKfbvzdufvu95v', '85454344589'),
                          (valid_phone, 'AKfbvzdufvu95v', ''),
                          (valid_phone, 'AKfbvzdufvu95v', '+79194737790'),
                          ])
def test_new_password_phone(driver, username, password, username_rep):

    page = Page(driver)

    # Вводим данные.
    page.username.send_keys(username)
    page.password.send_keys(password)

    # Входим в аккаунт.
    page.btn.click()
    # Переходим к востановлению пароля.
    page.fog_pass.click()

    page_first = page.get_current_url()

    # Вводим почту для востановления аккаунта
    page.username.send_keys(username_rep)

    page.btn.click()

    sec_page = page.get_current_url()

    if username_rep == '':
        assert page_first == sec_page  # Проверяем, что после нажания кнопки "Вход", адрес страницы не изменился
    else:
        err_msg = page.error
        assert err_msg.get_text() == "Неверный логин или текст с картинки"  # Проверяем, что на странице появилось высветилось соответствующее сообщение.
