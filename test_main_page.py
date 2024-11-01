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
from .pages.basket_page import BasketPage



@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()        # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()         # выполняем метод страницы — переходим на страницу логина
        print("успешно прошел тест test_guest_can_go_to_login_page")
        
        
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        print("успешно прошел тест test_guest_should_see_login_link")
    
    
def test_guest_can_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()  
    page.should_be_login_page()
    print("успешно прошел тест test_guest_can_see_login_page")
    
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open() 
    # перешли на страницу корзины (теперь можно применять методы из basket_page.py)
    page.go_to_basket_page()
    time.sleep(5)
    # инициализируем другой Page Object т.к. теперь действуем на другой странице, передаем в конструктор экземпляр драйвера и url адрес
    page = BasketPage(browser, link)
    page.should_v_korzine_ne_dolsho_bit_tovarov()
    page.should_be_message_vasha_korzina_pysta()
    print("успешно прошел тест test_guest_cant_see_product_in_basket_opened_from_main_page")