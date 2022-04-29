from selenium import webdriver
from selenium.webdriver.common.by import By


class ConfirmationPage:

    panier_selector = '#nav-cart'

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def openCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.panier_selector).click()
