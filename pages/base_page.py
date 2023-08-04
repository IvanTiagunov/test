from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    SEARCH_LINE = (By.ID, 'text')

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://ya.ru")

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find element by locator {locator}")
    def find_search_line(self):
        return self.find_element(self.SEARCH_LINE)