import pytest
from selenium.webdriver.common.by import By


def test_type_in_box(browser, my_text=None):
    if my_text is None:
        my_text = "Some text is there"
    box = browser.find_element(By.ID, "APjFqb")
    box.send_keys(my_text)
    text = box.get_attribute("value")
    assert text == "Some text is there"


def test_redirected_url(browser, my_text=None):
    if my_text is None:
        my_text = "ukraine"
    box = browser.find_element(By.ID, "APjFqb")
    box.send_keys(my_text)
    search_button = browser.find_element(By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b")
    search_button.click()
    assert "ukraine" in browser.current_url


def test_finding_item(browser, my_text=None):
    if my_text is None:
        my_text = "ukraine"
    box = browser.find_element(By.ID, "APjFqb")
    box.send_keys(my_text)
    search_button = browser.find_element(By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b")
    search_button.click()
    searched_item = browser.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[6]/div/div/div/div/div/div[1]/div/div/span/a/h3').text
    assert searched_item == "Official website of Ukraine"
