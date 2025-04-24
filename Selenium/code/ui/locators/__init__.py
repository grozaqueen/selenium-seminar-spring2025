from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')



class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )
    EVENTS = (By.ID, 'events')
    READ_MORE = (By.CSS_SELECTOR, 'a.readmore')


class LoginPageLocators(BasePageLocators):
    MODAL = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]")
    OPEN_MODAL_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/p[2]/button")
    CLOSE_MODAL_BUTTON = (By.XPATH, "/html/body/div/div/div[1]/div[2]/button")

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти с паролем']")

    ERROR_MESSAGE = (By.CLASS_NAME, "InputError__SError-sc-1ysghu0-0.ifUQKk")


class EventsPageLocators(BasePageLocators):
    pass
