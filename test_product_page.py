import pytest
import time
import math
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

   
@pytest.mark.xfail    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()        # открываем страницу
    page.add_to_cart()
    page.should_not_be_success_message()
    print("тест test_guest_cant_see_success_message_after_adding_product_to_basket ожидаемо падает т.к. при добавлении товара в козину ПОЯВЛЯЕТСЯ сообщение об успешном добавлении")
    
    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()        # открываем страницу   
    page.should_not_be_success_message()
    print("Проверяем, что нет сообщения об успехе _так_и_должно_быть_так_как_просто_открыли_страницу_с_товаром")
    print("Успешно прошел тест test_guest_cant_see_success_message")
    
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()    # открываем страницу
    page.add_to_cart()
    page.should_element_dolshen_ischezat()
    print("тест test_message_disappeared_after_adding_product_to_basket ожидаемо падает т.к. сообщение о добавл. товара в корзину корректно не исчезает через 10 секунд")

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    print("Успешно прошел тест test_guest_should_see_login_link_on_product_page")
    
   
    
@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Откроем страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        
        # Зарегистрируем нового пользователя
        email = str(time.time()) + "@fakemail.org"
        password = "strong_password"
        # вызываем метод для регистрации нового пользователя
        page.register_new_user(email, password)
        print("успешно зарегистрировали нового пользователя")
        
        # Проверим, что пользователь авторизован
        page.should_be_authorized_user()  
        print("успешно проверили, что польователь авторизован")        
       
    
    
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()        # открываем страницу   
        page.should_not_be_success_message()
        print("Проверяем, что нет сообщения об успехе _так_и_должно_быть_так_как_просто_открыли_страницу_с_товаром")
        print("Успешно прошел тест test_user_cant_see_success_message")
    
    
    
   
    
@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()        # открываем страницу
    page.add_to_cart() # через Page Object вызвал метод add_to_cart, который нажимает кнопку "Добавить в корзину"
    print("успешно добавили товар в корзину")   
    page.solve_quiz_and_get_code()
    print("успешно решили задачу и получили код") 
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
    print("успешно прошел тест test_user_can_add_product_to_basket")    
        
@pytest.mark.need_review         
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()        # открываем страницу
    page.add_to_cart() # через Page Object вызвал метод add_to_cart, который нажимает кнопку "Добавить в корзину"
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
    print("успешно прошел тест test_guest_can_add_product_to_basket")
        
        
@pytest.mark.need_review         
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()    # открываем страницу 
    # перешли на страницу корзины (теперь можно применять методы из basket_page.py)
    page.go_to_basket_page()
    page = BasketPage(browser, link)
    page.should_v_korzine_ne_dolsho_bit_tovarov()
    page.should_be_message_vasha_korzina_pysta()
    print("успешно прошел тест test_guest_cant_see_product_in_basket_opened_from_product_page")
        
        
@pytest.mark.need_review         
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()        # открываем страницу
    page.go_to_login_page()
    print("успешно перешли на страницу логина")
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()         # выполняем метод страницы — переходим на страницу логина
    print("успешно проверили, что на странице логина есть необходимые элементы и ссылки")
    print("успешно прошел тест test_guest_can_go_to_login_page_from_product_page")

