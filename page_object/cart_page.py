from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



class CartPage:

    quantity_select = "select[name='quantity']"


    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.quantity_select_element = Select(
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.quantity_select)))
        )

    def changeQuantity(self, quantity: str):
        self.quantity_select_element.select_by_value(quantity)

    def getQuantity(self):
        return self.quantity_select_element.first_selected_option.text