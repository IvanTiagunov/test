import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import dotenv_values

config = dotenv_values(".env")


@pytest.fixture(scope="function")
def browser():
    # Создаем экземпляр веб-драйвера
    driver_file = config.get('PATH_TO_DRIVER')
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

