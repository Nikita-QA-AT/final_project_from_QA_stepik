from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_vasha_korzina_pysta(self):
    # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*BasketPageLocators.MESSAGE_IN_BASKET), (
            "soobsheniya v korzine nety")
        print("сообщение при переходе в корзину присутствует")
        soobsheniye = self.browser.find_element(*BasketPageLocators.MESSAGE_IN_BASKET).text
        print('soobsheniye =', soobsheniye)
        # Проверяем, что сообщение включает в себя текст 
        assert "Ваша корзина пуста" in soobsheniye or "Your basket is empty" in soobsheniye, "текст не совпадает"
        print("успешно проверили что есть текст Ваша корзина пуста")
        
        
        
        
    def should_v_korzine_ne_dolsho_bit_tovarov(self):
    # проверяем, что блок с добавленными товарами отсутствует
        assert self.is_not_element_present(*BasketPageLocators.BLOK_S_TOVARAMI_V_KORZINE), (
            "blok s tovarami v korzine poyavilsya sledovatelno korzina ne pysta")
        print("успешно проверили что в корзине нет товаров")