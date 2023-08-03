import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()
   driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   driver.get('https://b2c.passport.rt.ru/auth')

   yield driver

   driver.quit()


