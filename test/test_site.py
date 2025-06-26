import time
from pages.cart import CartPage
from pages.homepage import HomePage
from pages.product import ProductPage



def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')


def test_open_lumia_1520(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_lumia_1520()
    product_page = ProductPage(browser)
    product_page.check_title_is('Nokia lumia 1520')


def test_open_nexus6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_nexus6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Nexus 6')


def test_open_galaxy_s7(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s7()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s7')


def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    # browser.get('https://demoblaze.com/')
    homepage.click_monitor()
    # monitor_link = browser.find_element(By.XPATH, '//a[text()="Monitors"]')
    # monitor_link.click()
    time.sleep(1)  #Вынужденная мера(
    homepage.check_products_count(2)
    # monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    # assert len(monitors) == 2


def test_six_laptops(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_laptops()
    time.sleep(1)
    homepage.check_products_count(6)


def test_seven_phones(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_phones()
    time.sleep(1)
    homepage.check_products_count(7)


def test_add_to_cart_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.add_to_cart()
    product_page.go_to_cart()
    cart_page = CartPage(browser)
    # cart_page.check_price("360")
    cart_page.delete_product_from_cart()


def test_check_home_button(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.go_to_home()
    homepage = HomePage(browser)
    homepage.check_home(9)








