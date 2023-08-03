import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

driver_file = r'chromedriver.exe' # path to YandexDriver
service = Service(executable_path=driver_file)

#ua = UserAgent()

options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.1.1140 Yowser/2.5 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://ya.ru")


# нахожу поисковую строку
search_line_elements = driver.find_elements(By.XPATH, value="//input[@class='search3__input mini-suggest__input']")

time.sleep(1000)
# проверяю, что строка существует
assert len(search_line_elements) != 0

input_line = search_line_elements[0]

input_line.click()

input_line.send_keys('Тензор')
time.sleep(3)
input_line.send_keys(Keys.ENTER)

time.sleep(100)