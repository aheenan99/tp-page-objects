from selenium import webdriver
from selenium.webdriver.common.by import By


class BooksPage:
    nouveau_livre_selector = "li.octopus-pc-item"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def selectFirstBookNouveautes(self):
        self.driver.find_elements(By.CSS_SELECTOR, self.nouveau_livre_selector)[0].click()
