from page_object.home_page import HomePage
from page_object.books_page import BooksPage
from page_object.product_page import ProductPage
from page_object.confirmation_page import ConfirmationPage
from page_object.cart_page import CartPage

from selenium import webdriver


def test_amazon1():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    driver.maximize_window()
    driver.quit()

def test_page_object():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    driver.maximize_window()

    homePage = HomePage(driver)
    homePage.closeCookies()
    homePage.openAllMenu()
    homePage.openBookCategory()
    homePage.openAllBooks()
    booksPage = BooksPage(driver)
    booksPage.selectFirstBookNouveautes()
    productPage = ProductPage(driver)
    productPage.addToCart()
    confirmationPage = ConfirmationPage(driver)
    confirmationPage.openCart()
    target_quantity = "2"
    cartPage = CartPage(driver)
    cartPage.changeQuantity(target_quantity)
    assert cartPage.getQuantity() == target_quantity


