import logging
import time

from selenium.webdriver import Keys

from pages.yandex_search import SearchPage

logger = logging.getLogger(__name__)

def test_successful_search(browser):
    search_page = SearchPage(browser)

    search_line = search_page.find_search_line()
    # logger.info(str(search_line.get_attribute('placeholder')))

    assert search_line != None

    search_line.send_keys("Тензор")

    suggestions = search_page.find_suggestions()
    logger.info("Список подсказок: {}".format(', '.join(map(lambda elem: elem.text, suggestions))))

    assert len(suggestions) > 0

    search_line.send_keys(Keys.ENTER)
    time.sleep(3)
    # logger.info(f"Текущаю страница: {browser.current_url}")

    assert "No results found." not in browser.page_source

    first_link = search_page.find_first_search_result()
    assert first_link.get_attribute("href") == "https://tensor.ru/"


