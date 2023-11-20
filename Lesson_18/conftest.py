import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get("https://google.com.ua")
    yield driver
    driver.close()
