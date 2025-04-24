from selenium.webdriver.support import expected_conditions as EC

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.events_page import EventsPage
import os
from dotenv import load_dotenv

load_dotenv()

class MainPage(BasePage):
    locators = basic_locators.MainPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.url = os.getenv("FEED_URL")
        print(f"MainPage: URL из .env = {self.url}")  # Отладка

    def get_username(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".username"))).text

    @allure.step("Переход на страницу событий")
    def go_to_events_page(self):
        self.click(self.locators.EVENTS)
        return