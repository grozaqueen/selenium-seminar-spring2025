import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure
from ui.pages.base_page import PageNotOpenedException
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
import os
from dotenv import load_dotenv
import time

load_dotenv()
print(f"Тест: LOGIN_URL = {os.getenv('LOGIN_URL')}")  # Отладка


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        if self.authorize:
            self.login_page.open()


class TestLogin(BaseCase):
    authorize = True

    @allure.title("Тест успешной авторизации через email/пароль")
    @allure.step("Проверка перенаправления и отображения элементов главной страницы")
    def test_successful_login_with_email_password(self):
        self.login_page.open_login_modal()
        self.login_page.login_with_email_password(
            os.getenv("VALID_EMAIL"),
            os.getenv("VALID_PASSWORD")
        )
        try:
            self.main_page.is_opened()
        except PageNotOpenedException:
            raise AssertionError(f"Страница {self.main_page.url} не открылась после авторизации")

        username = self.main_page.get_username()
        assert username == "Юлия Волкова", f"Ожидалось имя 'Юлия Волкова', но получено '{username}'"

    @allure.title("Тест неуспешной авторизации с неверным паролем")
    def test_unsuccessful_login_with_wrong_password(self):
        self.login_page.open_login_modal()
        self.login_page.login_with_email_password(
            os.getenv("VALID_EMAIL"),
            "wrong_password"
        )

        error_message = self.login_page.get_error_message()
        assert error_message == "Пользователь с такими данными не найден", "Ожидалось сообщение об ошибке"
        assert os.getenv(
            "FEED_URL") not in self.driver.current_url, "Произошло неожиданное перенаправление на страницу ленты"

    @allure.title("Тест закрытия модального окна без входа")
    def test_close_login_modal(self):
        self.login_page.open_login_modal()

        self.login_page.close_modal()

        modal_present = len(self.driver.find_elements(By.CLASS_NAME, "Modal__SChildrenWrapper-sc-1grozrf-3.dKrCGz")) == 0
        assert modal_present, "Модальное окно не закрылось после нажатия кнопки закрытия"

        assert self.driver.current_url == os.getenv("BASE_URL"), "URL изменился после закрытия модального окна"
