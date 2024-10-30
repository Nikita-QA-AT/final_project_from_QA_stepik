from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_CART_SELECTOR = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alert-success:first-of-type div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info div.alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    
    
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    KNOPKA_POSMOTRET_KORSINY_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    
    
    
class BasketPageLocators():    
    MESSAGE_IN_BASKET = (By.CSS_SELECTOR, "#content_inner p")