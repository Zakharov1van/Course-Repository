from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import compare_links
from data import compare_names


def test_menu_names(browser):
    menu_dict = {}
    wait = WebDriverWait(browser, 20)
    for number_id in range(3, 9):
        menu_name = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="ui-id-{number_id}"]')))
        actions = ActionChains(browser)
        actions.move_to_element(menu_name).perform()
        submenu_items = menu_name.find_elements(By.XPATH, f'//*[contains(@class, "level1 nav-{number_id - 2}")]')
        if len(submenu_items) > 0:
            submenu_dir = {}
            for item in submenu_items:
                item_name = item.text
                actions.move_to_element(item).perform()
                subsubmenu_items = item.find_elements(By.XPATH, f'//*[contains(@class, "level2 nav-{number_id - 2}")]')
                if len(subsubmenu_items) > 0:
                    subsub_names = []
                    for i in subsubmenu_items:
                        name = i.text
                        subsub_names.append(name)
                    subsub_lst = list(filter(bool, subsub_names))
                    submenu_dir[item_name] = subsub_lst
                else:
                    submenu_dir[item_name] = None
            menu_dict[menu_name.text] = submenu_dir
        else:
            menu_dict[menu_name.text] = None

    assert menu_dict == compare_names


def test_click(browser):
    menu_links = []
    wait = WebDriverWait(browser, 20)
    menu_name = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="ui-id-3"]')))
    menu_items = browser.find_elements(By.XPATH, f'//*[contains(@role, "menuitem")]')
    for item in menu_items:
        menu_link = item.get_attribute("href")
        menu_links.append(menu_link)

    for link in menu_links:
        browser.get(link)

    assert menu_links == compare_links


def test_drag_and_drop(drag_drop):
    wait = WebDriverWait(drag_drop, 20)
    drag = wait.until(EC.element_to_be_clickable((By.XPATH, "//header[text()='A']")))
    drop = wait.until(EC.element_to_be_clickable((By.XPATH, "//header[text()='B']")))
    actions = ActionChains(drag_drop)
    actions.drag_and_drop(drag, drop).perform()
    column_a = drag_drop.find_element(By.ID, "column-a").text
    assert column_a == "B"
