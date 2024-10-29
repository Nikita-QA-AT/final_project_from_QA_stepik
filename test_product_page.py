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



def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()        # открываем страницу
    time.sleep(2)
    page.add_to_cart() # через Page Object вызвал метод add_to_cart, который нажимает кнопку "Добавить в корзину"
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.should_be_message_about_adding()
    time.sleep(2)
    page.should_be_message_basket_total()
    time.sleep(2)