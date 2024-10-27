from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    
    def add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_SELECTOR)
        button_add_to_cart.click()
    