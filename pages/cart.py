from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    # def check_price(self, expected_price):
    #     price_element = self.wait.until(EC.invisibility_of_element_located((By.XPATH, '//td[contains(@class, "price") or @id="totalp"]')))
    #     price = price_element.text.strip()
    #     assert price == str(expected_price), f"Ожидалась цена {expected_price}, получено {price}"

    def delete_product_from_cart(self):
        delete_from_cart = self.browser.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[4]/a')
        delete_from_cart.click()

