from selenium.webdriver.common.by import By



class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://demoblaze.com/')

    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()

    def click_lumia_1520(self):
        lumia_1520 = self.browser.find_element(By.XPATH, '//a[text()="Nokia lumia 1520"]')
        lumia_1520.click()

    def click_nexus6(self):
        nexus6 = self.browser.find_element(By.XPATH, '//a[text()="Nexus 6"]')
        nexus6.click()

    def click_galaxy_s7(self):
        galaxy_s7 = self.browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s7"]')
        galaxy_s7.click()

    def click_monitor(self):
        monitor_link = self.browser.find_element(By.XPATH, '//a[text()="Monitors"]')
        monitor_link.click()

    def check_products_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count

    def click_laptops(self):
        laptops_link = self.browser.find_element(By.XPATH, '//a[text()="Laptops"]')
        laptops_link.click()

    def click_phones(self):
        phones_link = self.browser.find_element(By.XPATH, '//a[text()="Phones"]')
        phones_link.click()

    def click_home(self):
        home_link = self.browser.find_element(By.XPATH, '//a[text()="Home"]')
        home_link.click()

    def check_home(self, count):
        cards = self.browser.find_elements(By.CSS_SELECTOR, '.card')
        assert len(cards) == count

    # def click_next(self):
    #     next_button = self.browser.find_element(By.XPATH, '//a[contains(@class, "page-link") and contains(text(), "Next")]')
    #     next_button.click()


