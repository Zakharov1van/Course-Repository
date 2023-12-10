import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .. selenium_all import MySelenium
from .. data import free_trial_links
from .. data import adobe_links
from .. data import header_links
from .. data import follow_links
from .. data import footer_links


@pytest.mark.parametrize("base_url", ["https://www.behance.net/gallery/18988225/B-Yoga-Website"])
def test_base_url(base_url):
    page = MySelenium()
    page.get_page(base_url)
    assert page.get_current_url() == "https://www.behance.net/gallery/18988225/B-Yoga-Website"
    page.close_browser()


@pytest.mark.parametrize("base_url", ["https://www.behance.net/gallery/18988225/B-Yoga-Website"])
def test_header_links(base_url):
    page = MySelenium()
    page.get_page(base_url)
    found_links = page.check_links_in_node("//ul[@class = 'PrimaryNav-coreNavigation-iAB']")
    assert found_links == header_links
    page.close_browser()


@pytest.mark.parametrize("base_url", ["https://www.behance.net/gallery/18988225/B-Yoga-Website"])
def test_footer_links(base_url):
    page = MySelenium()
    page.get_page(base_url)
    found_links = page.check_links_in_node("//footer[@class = 'StaticFooter-footerContainer-jf4']")
    assert found_links == footer_links
    page.close_browser()


@pytest.mark.parametrize("base_url", ["https://www.behance.net/gallery/18988225/B-Yoga-Website"])
def test_links_free_trial_dropdown(base_url):
    page = MySelenium()
    page.get_page(base_url)
    found_links = page.dropdown_menu("//button[@class='Btn-button-CqT Btn-base-L7P Btn-normal-If5 PrimaryNav-freeTrialButton-TwI e2e-Nav-free-trial']", "//div[@class = 'AdobeCheckoutPopoverContent-root-ogZ']")
    assert found_links == free_trial_links
    page.close_browser()


@pytest.mark.parametrize("base_url", ["https://www.behance.net/gallery/18988225/B-Yoga-Website"])
def test_links_adobe_dropdown(base_url):
    page = MySelenium()
    page.get_page(base_url)
    found_links = page.dropdown_menu("//div[@class = 'PrimaryNav-adobeLogo-VeZ']", "//div[@class = 'NavPopoverContent-menu-kr7']")
    assert found_links == adobe_links
    page.close_browser()


@pytest.mark.parametrize("base_url", ["https://www.behance.net/gallery/18988225/B-Yoga-Website"])
def test_links_notification_dropdown(base_url):
    page = MySelenium()
    page.get_page(base_url)
    found_links = page.dropdown_menu("//button[@class = 'PrimaryNav-link-hxX PrimaryNav-userControlLink-JRN']", "//div[@class = 'NotificationsList-listWrapper-ctr']")
    assert found_links == ["https://www.behance.net/blog/visual-trends-2023"]
    page.close_browser()


@pytest.mark.parametrize("base_url", ["https://www.behance.net/gallery/18988225/B-Yoga-Website"])
def test_links_follow(base_url):
    page = MySelenium()
    page.get_page(base_url)
    found_links = page.dropdown_menu("//div[@class = 'Avatar-root-Ic4 Project-toolsAvatar-p2p']", "//div[@class = 'Popover-content-rnw Popover-light-WK0 Popover-hideMobile-KuU Popover-hideTablet-Se9 Miniprofile-content-S7Y }']")
    assert found_links == follow_links
    page.close_browser()


@pytest.mark.parametrize("base_url", ["https://www.behance.net/gallery/18988225/B-Yoga-Website"])
def test_expanded_comments(base_url):
    page = MySelenium()
    page.get_page(base_url)
    page.scroll_to_element("//div[@data-id = '43938213']")
    number_of_comments = page.check_comments_button("//div[@class = 'ProjectComments-seeMore-QA7']","//li[@class = 'ProjectComments-projectCommentContainer-pzz']")
    time.sleep(10)
    assert number_of_comments == 20
    page.close_browser()

@pytest.mark.parametrize("base_url, button_xpath", [("https://www.behance.net/gallery/18988225/B-Yoga-Website", "//div[@class = 'FollowButtonLegacy-legacyButton-mPH Project-captionFollow-fY4']"),
                                                    ("https://www.behance.net/gallery/18988225/B-Yoga-Website", "//div[@class = 'IconMessageButton-regularMessageText-PEu']"),
                                                    ("https://www.behance.net/gallery/18988225/B-Yoga-Website", "//div[@class = 'Tooltip-wrapper-Uzv Project-tooltip-PUI Project-collection-y5x']"),
                                                    ("https://www.behance.net/gallery/18988225/B-Yoga-Website", "//button[@class='Btn-button-CqT Btn-tertiary-Z8Q Btn-normal-If5 js-adobeid-signin e2e-PrimaryNav-Signin']"),
                                                     ("https://www.behance.net/gallery/18988225/B-Yoga-Website", "//button[@class='Btn-button-CqT Btn-primary-wt8 Btn-normal-If5 js-adobeid-signup e2e-PrimaryNav-signup']")])
def test_first_screen_buttons(base_url, button_xpath):
    page = MySelenium()
    page.get_page(base_url)
    page.click_on_button(button_xpath)
    time.sleep(3)
    assert "https://auth.services.adobe.com" in page.get_current_url()
    page.close_browser()

@pytest.mark.parametrize("base_url, xpath", [("https://www.behance.net/gallery/18988225/B-Yoga-Website", "//div[@class = 'FollowButtonLegacy-legacyButton-mPH']"),
                                             ("https://www.behance.net/gallery/18988225/B-Yoga-Website", "//div[@class = 'Btn-labelWrapper-_Re MessageButton-buttonLabel-j2x undefined']")])
def test_follow_and_massage_buttons(base_url, xpath):
    page = MySelenium()
    page.get_page(base_url)
    page.scroll_to_element("//div[@class = 'ProjectComments-seeMore-QA7']")
    page.click_on_button(xpath)
    time.sleep(3)
    assert "https://auth.services.adobe.com" in page.get_current_url()
    page.close_browser()
