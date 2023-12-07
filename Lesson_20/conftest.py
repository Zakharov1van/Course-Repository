import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com")
    yield driver
    driver.close()


@pytest.fixture
def drag_drop():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    yield driver
    driver.close()
