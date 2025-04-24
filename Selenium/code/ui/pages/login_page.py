import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ..locators import LoginPageLocators

load_dotenv()

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = os.getenv("LOGIN_URL")
        print(f"LoginPage: URL из .env = {self.url}")
        if not self.url:
            raise ValueError("LOGIN_URL не найден в .env файле")

    def open(self):
        print(f"Открываем URL: {self.url}")
        self.driver.get(self.url)
        self.is_opened()

    def open_login_modal(self):
        print("Ищем модальное окно...")
        modal = self.find(LoginPageLocators.MODAL)
        print(f"Модальное окно найдено: {modal.is_displayed()}")
        self.click(LoginPageLocators.OPEN_MODAL_BUTTON)
        modal = self.find(LoginPageLocators.MODAL)
        assert modal.is_displayed(), "Модальное окно входа не отображается"

    def login_with_email_password(self, email, password):
        email_input = self.find(LoginPageLocators.EMAIL_INPUT)
        email_input.click()
        email_input.clear()
        email_input.send_keys(email)

        password_input = self.find(LoginPageLocators.PASSWORD_INPUT)
        password_input.click()
        password_input.clear()
        password_input.send_keys(password)

        self.click(LoginPageLocators.LOGIN_BUTTON)

    def close_modal(self):
        self.click(LoginPageLocators.CLOSE_MODAL_BUTTON)

    def get_error_message(self):
        error_message = self.find(LoginPageLocators.ERROR_MESSAGE)
        return error_message.text if error_message.is_displayed() else None