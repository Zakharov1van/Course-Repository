from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_print_menu_names(browser):
    wait = WebDriverWait(browser, 10)
    for item in range(1, 5):
        menu_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#menu > ul > li:nth-child({item}) > a")))
        item_name = menu_item.text
        print(item_name)


def test_menu_names(browser):
    menu_names = []
    wait = WebDriverWait(browser, 10)
    for item in range(1, 5):
        menu_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#menu > ul > li:nth-child({item}) > a")))
        item_name = menu_item.text
        menu_names.append(item_name)
        menu_item.click()
    assert menu_names == ["Home", "News", "Contact", "About"]
