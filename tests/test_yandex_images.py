import logging

from pages.yandex_images import ImagesPage

logger = logging.getLogger(__name__)


def test_images(browser):
    # Получение главной страницы
    page = ImagesPage(browser)
    # Клик по строке поиска для отображения кнопки меню
    page.find_search_line()
    # Проверка присутствия кнопки меню на странице
    menu_button = page.get_menu()
    assert menu_button.is_displayed()

    # Переход в раздел "Картинки"
    menu_button.click()
    page.click_image_button()
    # Проверка адреса страницы
    page.switch_the_page()
    assert page.driver.current_url == "https://ya.ru/images/"

    # Переход в первую отображаемую категорию
    category_name = page.click_and_get_first_category_name()
    # Проверка отображения названия категории в поле поиска
    search_line_value = page.get_search_line_value_after_image_choose()
    assert category_name == search_line_value

    # Переход к первой картинке в выбранной категории
    page.click_first_small_image()
    # Получение ссылки на первую картинку
    url_first_big_image = page.get_big_image_src()
    # Проверка корретной загрузки фото на странице
    assert page.check_big_image_exists()

    # Переход к следующей картинке
    page.click_next_image_button()
    # Проверка смены картинки
    url_second_big_image = page.get_big_image_src()
    assert url_first_big_image != url_second_big_image

    # Переход к предыдущей картинке
    page.click_previous_image_button()
    url_third_big_image = page.get_big_image_src()
    # Проверка первой картинки. Она должна остаться той же
    assert url_third_big_image == url_first_big_image
