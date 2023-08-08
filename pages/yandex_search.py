from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    SUGGESTIONS = (By.XPATH, "//ul[@class='mini-suggest__popup-content']/li")
    FIRST_RESULT_LINK = (By.XPATH, "(//li[contains(@class,'serp-item')]//a)[2]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_suggestions(self):
        return self.find_elements(self.SUGGESTIONS)

    def get_first_search_result(self):
        return self.find_element(self.FIRST_RESULT_LINK)
