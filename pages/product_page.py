from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage): 
    
    def add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_SELECTOR)
        button_add_to_cart.click()
    
    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print('product_name =', product_name)
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        print('message =', message)
        # Проверяем, что название товара присутствует в сообщении о добавлении
        # Это можно было бы сделать с помощью split() и сравнения строк,
        # Но не вижу необходимости усложнять код
        assert product_name == message, "No product name in the message"
        print("успешно проверели наличие названия книги в уведомлении о добавлении")
        
        
        
        
        
        
    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message about total price is not presented")
        # Затем получаем текст элементов для проверки
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print('product_price =', product_price)
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        print('message_basket_total =', message_basket_total)
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price == message_basket_total, "No product price in the message"
        print("успешно проверили что точная сумма стоимости книги входит в сообщении о стоимости корзины")
        
        
        
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
           "Success message is presented, but should not be"
           
           
    def should_element_dolshen_ischezat(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING, timeout=10), \
            "Element dolshen bil ischeznyt' no ne ischez"