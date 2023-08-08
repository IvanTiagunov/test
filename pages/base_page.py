from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    SEARCH_LINE = (By.ID, 'text')

    def __init__(self, driver):
        self.driver = driver
        # Переход на главную страницу
        self.driver.get("https://ya.ru")

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_search_line(self):
        elem = self.find_element(self.SEARCH_LINE)
        elem.click()
        return elem

    def find_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(locator))
        return element

    def find_clickable_and_click(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element
