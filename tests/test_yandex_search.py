import pytest
from pages.yandex_search import SearchPage

def test_successful_input(browser):
    browser.get("https://ya.ru")