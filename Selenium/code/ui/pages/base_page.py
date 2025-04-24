import time
import os
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ui.locators import basic_locators

load_dotenv()

class PageNotOpenedException(Exception):
    pass

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = os.getenv("BASE_URL")
        self.url = self.base_url  # Устанавливается по умолчанию, переопределяется в дочерних классах
        print(f"BasePage: base_url = {self.base_url}, url = {self.url}")  # Отладка

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url.startswith(self.url):
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()