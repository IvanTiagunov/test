
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import dotenv_values

config = dotenv_values(".env")


@pytest.fixture(scope="function")
def browser():
    # Создаем экземпляр веб-драйвера Chrome
    driver_file=r'chromedriver.exe'
    service = Service(executable_path=driver_file)
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)

    # Устанавливаем время неявного ожидания элементов на странице
    driver.implicitly_wait(10)

    # Используем инструкцию yield для предоставления веб-драйвера тестам и ожидания завершения тестов
    yield driver

    # Закрываем веб-драйвер после завершения каждого теста
    driver.quit()




#options.add_argument(f"--profile-directory={config.get('PROFILE_DIRECTORY')}")
#options.add_argument(f"--user-data-dir={config.get('USER_DATA_DIR')}")
# user_agent = config.get('USER_AGENT')
# options.add_argument(f"user-agent={user_agent}")
#options.add_argument("--disable-blink-features=AutomationControlled")

# driver.get("https://ya.ru")
#
# # нахожу поисковую строку
# search_line_elements = driver.find_elements(By.XPATH, value="//input[@class='search3__input mini-suggest__input']")
#
# from selenium.common.exceptions import NoSuchElementException
#
#
# # проверяю, что строка существует
# assert len(search_line_elements) != 0
#
# input_line = search_line_elements[0]
#
# input_line.click()
# time.sleep(2)
# input_line.send_keys('Тензор')
#
# #todo Изменить xpath value
# li = driver.find_element(By.XPATH,
#                          value="//ul[@class='mini-suggest__popup-content']/li[@class='mini-suggest__item']")
# print(li)


#https://vk.com/@iteapro-page-object-i-pytest-effektivnoe-testirovanie-veb-prilozheni#