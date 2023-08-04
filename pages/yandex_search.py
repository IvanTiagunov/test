from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    SUGGESTIONS = (By.XPATH, "//ul[@class='mini-suggest__popup-content']/li")
    FIRST_RESULT_LINK = (By.XPATH, "(//li[contains(@class,'serp-item')]//a)[2]")

    def __init__(self, driver):
        super().__init__(driver)

    def find_suggestions(self):
        return self.find_elements(self.SUGGESTIONS)

    def find_first_search_result(self):
        return self.find_element(self.FIRST_RESULT_LINK)
