import pytest
from selenium import webdriver


BASE_URL = "https://the-internet.herokuapp.com/floating_menu#home"


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(3)
    driver.get(BASE_URL)
    yield driver
    driver.close()
