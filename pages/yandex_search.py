from selenium.webdriver.common.by import By
class SearchPage:
    SEARCH_LINE = (By.XPATH, "//input[@class='search3__input mini-suggest__input']")

    def __init__(self, driver):
        self.driver = driver


    def find_search_line(self):
        self.driver.find_element(*self.SEARCH_LINE)