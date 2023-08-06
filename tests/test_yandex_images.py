import logging
import time
from pages.yandex_images import ImagesPage
logger = logging.getLogger(__name__)

# Todo заменить все time.sleep() методы на ожидание загрузки страницы.
def test_images(browser):
    # нажать на поисковую строку центре страницы
    page = ImagesPage(browser)
    time.sleep(6)

    search_line = page.find_search_line()
    search_line.click()
    # нажать на иконку меню
    menu_button = page.get_menu()
    assert menu_button.is_displayed()
    menu_button.click()

    image_button = page.get_image_button()

    image_button.click()

    time.sleep(3)
    # переключаем страницу
    page.switch_the_page()

    assert page.driver.current_url == "https://ya.ru/images/"

    category = page.get_first_category()
    category_name = category.get_attribute('data-grid-text')

    category.click()

    line = page.get_search_line_after_image_choose()

    assert category_name == line.get_attribute('value')

    small_image = page.get_first_small_image()
    small_image.click()

    first_big_image = page.get_big_image()

    time.sleep(2)

    no_error = page.get_no_error_message_on_image_loading()

    assert no_error

    url_first_big_image = first_big_image.get_attribute('src')

    next_button = page.get_next_image_button()
    next_button.click()

    time.sleep(2)

    url_second_big_image = page.get_big_image().get_attribute('src')

    assert url_first_big_image != url_second_big_image

    previous_button = page.get_previous_image_button()
    previous_button.click()

    url_third_big_image = page.get_big_image().get_attribute('src')

    assert url_third_big_image == url_first_big_image

