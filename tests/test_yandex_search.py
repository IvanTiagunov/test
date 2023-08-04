import logging
import time

from pages.yandex_search import SearchPage

logger = logging.getLogger(__name__)

def test_successful_serch(browser):
    search_page = SearchPage(browser)
    browser.get("https://ya.ru")

    search_line = search_page.find_search_line()
    logger.info(str(search_line.get_attribute('placeholder')))

    assert search_line != None

    search_line.send_keys("Тензор")

    suggestions = search_page.find_suggestions()
    logger.info("Список подсказок: {}".format(', '.join(map(lambda elem: elem.text, suggestions))))

    assert len(suggestions) > 0

    time.sleep(10)


