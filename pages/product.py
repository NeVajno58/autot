from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def check_title_is(self, title):
        page_title = self.browser.find_element(By.CSS_SELECTOR, 'h2')
        assert page_title.text == title

    def add_to_cart(self):
        add_to_cart_s6 = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Add to cart"]')))
        add_to_cart_s6.click()

    def go_to_cart(self):
        go_to_cart = self.browser.find_element(By.XPATH, '//a[text()="Cart"]')
        go_to_cart.click()

    def go_to_home(self):
        go_to_home = self.browser.find_element(By.XPATH, '//a[contains(@class, "nav-link") and contains(text(), "Home")]')
        go_to_home.click()
