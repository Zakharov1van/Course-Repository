import pytest
from ..selenium_all import MySelenium
from ..data import link_list
from ..data import title_list


@pytest.mark.parametrize("base_url", ["https://www.google.com.ua/?hl=uk"])
def test_base_url(base_url):
    page = MySelenium()
    page.get_page(base_url)
    assert page.get_current_url() == "https://www.google.com.ua/?hl=uk"


@pytest.mark.parametrize("base_url, param", [("https://www.google.com", "Hello, world!")])
def test_search_box(base_url, param):
    page = MySelenium()
    page.get_page(base_url)
    text_box = page.search_box(param)
    assert text_box == "Hello, world!"


@pytest.mark.parametrize("base_url, tag", [("https://www.google.com.ua/?hl=uk", "a")])
def test_all_links(base_url, tag):
    page = MySelenium()
    page.get_page(base_url)
    found_links = page.search_links_by_tag(tag)
    assert found_links == link_list


@pytest.mark.parametrize("base_url, tag", [("https://www.google.com.ua/?hl=uk", "a")])
def test_click(base_url, tag):
    page = MySelenium()
    page.get_page(base_url)
    found_links = page.search_links_by_tag(tag)
    page_titles = page.clicker_and_title_checker(found_links)
    assert page_titles == title_list
