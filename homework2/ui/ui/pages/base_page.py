
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.ui.locators.locators import BaseLocators

RETRY_COUNT = 3


class BasePage:
    locators = BaseLocators()

    def __init__(self, driver):
        self.driver = driver
        self.user = 'asktechnoatom@mail.ru'
        self.password = 'asktechnoatom'

    def find(self, locator, timeout=None):
        s = self.wait(timeout).until(EC.presence_of_all_elements_located(locator))
        if len(s) == 1:
            return self.wait(timeout).until(EC.presence_of_element_located(locator))
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def click(self, locator, timeout=None):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def authorization(self, user, password):
        self.find(self.locators.ENTER_BUTTON).click()
        user_field = self.find(self.locators.INPUT_NAME)
        user_field.clear()
        password_field = self.find(self.locators.INPUT_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)
        user_field.send_keys(user)
        self.find(self.locators.AUTHORIZATION_BUTTON).click()

