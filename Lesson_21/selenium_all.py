from selenium import webdriver
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
        element = wait.until(EC.element_to_be_clickable((By.ID, "APjFqb")))
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
