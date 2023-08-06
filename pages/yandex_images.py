import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from .base_page import BasePage



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

    # SECOND_BIG_IMAGE =
    def __init__(self, driver):
        super().__init__(driver)
        self.original_page_id = driver.current_window_handle

    def get_menu(self):
        return self.find_element(self.MENU_BUTTON)

    def get_image_button(self):
        return self.find_element(self.IMAGES_BUTTON)

    def get_first_category(self):
        return self.find_element(self.FIRST_CATEGORY_BUTTON)

    def get_search_line_after_image_choose(self):
        return self.find_element(self.SEARCH_LINE_AFTER_IMAGE_CHOOSE)

    def switch_the_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != self.original_page_id:
                self.driver.switch_to.window(window_handle)
                break

    def get_first_small_image(self):
        return self.find_element(self.FIRST_SMALL_IMAGE)

    def get_big_image(self):
        return self.find_element(self.BIG_IMAGE)

    def get_no_error_message_on_image_loading(self):
        return self.do_not_find_element(self.ERROR_MESSAGE_ON_IMAGE)

    def get_next_image_button(self):
        return self.find_element(self.NEXT_IMAGE_BUTTON)

    def get_previous_image_button(self):
        return self.find_element(self.PREV_IMAGE_BUTTON)