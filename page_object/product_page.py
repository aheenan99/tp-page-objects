from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductPage:

    ajouter_au_panier_selector = '#add-to-cart-button:first-of-type'

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def addToCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.ajouter_au_panier_selector).click()
