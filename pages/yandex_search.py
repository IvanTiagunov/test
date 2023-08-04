from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    SEARCH_LINE = (By.ID, 'text')
    SUGGESTIONS = (By.XPATH, "//ul[@class='mini-suggest__popup-content']/li")
    def __init__(self, driver):
        self.driver = driver


    def find_element(self,locator,time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                               message=f"Can't find element by locator {locator}")
    def find_elements(self,locator,time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                               message=f"Can't find element by locator {locator}")

    def find_search_line(self):
        return self.find_element(self.SEARCH_LINE)

    def find_suggestions(self):
        return self.find_elements(self.SUGGESTIONS)

    # def input_phrase(self):
    #     self.