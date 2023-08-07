import logging
import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

logger = logging.getLogger(__name__)


class ImagesPage(BasePage):
    MENU_BUTTON = (By.XPATH, "//li[@class='services-suggest__list-item-more']/a")
    IMAGES_BUTTON = (By.XPATH, "//a[@aria-label='Картинки']")
    FIRST_CATEGORY_BUTTON = (By.XPATH, "//div[@class='PopularRequestList-Item PopularRequestList-Item_pos_0']")
    SEARCH_LINE_AFTER_IMAGE_CHOOSE = (By.XPATH, "//span[@class='input__box']/input")
    FIRST_SMALL_IMAGE = (By.XPATH, "//div[@class='serp-item__preview']/a")
    BIG_IMAGE = (By.XPATH, "//img[@class='MMImage-Origin']")
    ERROR_MESSAGE_ON_IMAGE = (By.XPATH, "//div[contains(@class,'MediaViewer-ViewMessage')]")
    NEXT_IMAGE_BUTTON = (By.XPATH, "(//i[@class='CircleButton-Icon'])[4]")
    PREV_IMAGE_BUTTON = (By.XPATH, "(//i[@class='CircleButton-Icon'])[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.original_page_id = driver.current_window_handle

    def get_menu(self):
        return self.find_clickable(self.MENU_BUTTON)

    def click_image_button(self):
        return self.find_clickable_and_click(self.IMAGES_BUTTON)

    def click_and_get_first_category_name(self):
        category = self.find_element(self.FIRST_CATEGORY_BUTTON)
        category_name = category.get_attribute('data-grid-text')
        category.click()
        return category_name

    def get_search_line_value_after_image_choose(self):
        return self.find_element(self.SEARCH_LINE_AFTER_IMAGE_CHOOSE).get_attribute('value')

    def switch_the_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != self.original_page_id:
                self.driver.switch_to.window(window_handle)
                break

    def click_first_small_image(self):
        return self.find_clickable_and_click(self.FIRST_SMALL_IMAGE)

    def get_big_image_src(self):
        time.sleep(2)
        return self.find_element(self.BIG_IMAGE).get_attribute('src')

    def get_no_error_message_on_image_loading(self):
        return self.do_not_find_element(self.ERROR_MESSAGE_ON_IMAGE)

    def click_next_image_button(self):
        return self.find_clickable_and_click(self.NEXT_IMAGE_BUTTON)

    def click_previous_image_button(self):
        return self.find_clickable_and_click(self.PREV_IMAGE_BUTTON)
