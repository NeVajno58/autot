from numpy.f2py.rules import options
from selenium.webdriver.common.by import By
import time
from pages.homepage import HomePage
from pages.product import ProductPage



def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galgaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')


def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    # browser.get('https://demoblaze.com/')
    homepage.click_monitor()
    # monitor_link = browser.find_element(By.XPATH, '//a[text()="Monitors"]')
    # monitor_link.click()
    time.sleep(1)
    homepage.check_products_count(2)
    # monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    # assert len(monitors) == 2