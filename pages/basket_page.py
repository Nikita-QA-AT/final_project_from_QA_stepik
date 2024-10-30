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
        assert "Ваша корзина пуста" in soobsheniye, "текст не совпадает"
        print("успешно проверили что текст Ваша корзина пуста")