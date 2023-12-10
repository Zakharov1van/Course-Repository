import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MySelenium:
    def __init__(self, browser_type = "chrome"):
        self.browser_type = browser_type
        self.driver = self._get_driver()

    def _get_driver(self):
        if self.browser_type == "chrome":
            driver = webdriver.Chrome()
        elif self.browser_type == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")
        return driver

    def get_page(self, url):
        self.driver.get(url)

    def search_box(self, my_text):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'SearchTypeahead-searchContainer-Owv SearchTypeahead-isTypeaheadEnabled-xOv']")))
        element.click()
        element.clear()
        element.send_keys(my_text)
        return element.get_attribute("value")

    def search_links_by_tag(self, tag_name):
        item_lst = self.driver.find_elements(By.TAG_NAME, tag_name)
        link_lst = []
        for item in item_lst:
            link = item.get_attribute("href")
            if link is not None:
                link_lst.append(link)
        return link_lst

    def search_iframe_links(self):
        links = []
        wait = WebDriverWait(self.driver, 20)
        dropdown = self.driver.find_element(By.XPATH, "//a[@class='gb_d']")
        dropdown.click()
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@name='app']")))
        iframe_items = self.driver.find_elements(By.XPATH, "//a[@href]")
        for item in iframe_items:
            link = item.get_attribute("href")
            links.append(link)
        return links

    def clicker_and_title_checker(self, links):
        titles = []
        for link in links:
            self.driver.get(link)
            title = self.driver.title
            titles.append(title)
        return titles

    def get_current_url(self):
        return self.driver.current_url

    def close_browser(self):
        self.driver.quit()


    def dropdown_menu(self, xpath, container):
        dropdown_links = []
        actions = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)
        free_trial = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        actions.move_to_element(free_trial).perform()
        time.sleep(3)
        item_window = self.driver.find_element(By.XPATH, container)
        item_links = item_window.find_elements(By.XPATH, ".//a")
        for item in item_links:
            link = item.get_attribute("href")
            if link is not None:
                dropdown_links.append(link)
        return dropdown_links

    def scroll_to_element(self, element_xpath):
        self.driver.implicitly_wait(2)
        element = self.driver.find_element(By.XPATH, element_xpath)
        self.driver.implicitly_wait(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def check_comments_button(self, button_xpath, items_xpath):
        button = self.driver.find_element(By.XPATH, button_xpath)
        self.driver.implicitly_wait(3)
        button.click()
        time.sleep(3)
        new_comments = self.driver.find_elements(By.XPATH, items_xpath)
        return len(new_comments)

    def check_links_in_node(self, node_xpath):
        links = []
        wait = WebDriverWait(self.driver, 20)
        node = wait.until(EC.presence_of_element_located((By.XPATH, node_xpath)))
        node_items = node.find_elements(By.XPATH, ".//a")
        for item in node_items:
            link = item.get_attribute("href")
            links.append(link)
        return links

    def click_on_button(self, button_xpath):
        wait = WebDriverWait(self.driver, 20)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        button.click()

    def get_text_iframe(self, xpath):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Оформление заказа Adobe']")))
        text = wait.until(EC.presence_of_element_located((By.XPATH, xpath))).text
        return text

    def get_page_title(self):
        return self.driver.title

    def get_text_from_selector(self, xpath, items_xpath):
        wait = WebDriverWait(self.driver, 20)
        func_list = []
        selector = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(selector).perform()
        time.sleep(3)
        selector_items = self.driver.find_elements(By.XPATH, items_xpath)
        for item in selector_items:
            text = item.text
            func_list.append(text)
        return func_list

    def open_selector(self, xpath):
        wait = WebDriverWait(self.driver, 20)
        selector = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        actions = ActionChains(self.driver)
        actions.move_to_element(selector).perform()
