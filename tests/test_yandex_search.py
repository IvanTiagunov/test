import logging
import time

from selenium.webdriver import Keys

from pages.yandex_search import SearchPage

logger = logging.getLogger(__name__)


def test_successful_search(browser):
    # Получение главной страницы
    search_page = SearchPage(browser)
    # Получение поля поиска
    search_line = search_page.find_search_line()
    # Проверка наличия поля поиска
    assert search_line.is_displayed()

    # Ввод в поиск Тензор
    search_line.send_keys("Тензор")
    # Получение списка подсказок
    suggestions = search_page.get_suggestions()
    # Вывод в лог списка подсказок
    logger.info("Список подсказок: {}".format(', '.join(map(lambda elem: elem.text, suggestions))))
    # Проверка существования списка
    assert len(suggestions) > 0

    # Нажатие клавиши enter
    search_line.send_keys(Keys.ENTER)
    # Проверка существования страницы результатов поиска
    assert "No results found." not in browser.page_source

    # Получение первой ссылки в поисковой выдаче
    first_link = search_page.get_first_search_result()
    # Проверка, что первая ссылка ведёт на официальный сайт
    assert "https://tensor.ru/" in first_link.get_attribute("href")
