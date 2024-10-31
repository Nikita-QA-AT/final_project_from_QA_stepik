from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        print(f"Current URL: {self.browser.current_url}")
        assert "login" in self.browser.current_url, "Login URL is incorrect"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
        
        
    def register_new_user(self, email, password):
        #вводим email
        pole_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
        print("успешно ввели email")
        #вводим пароль 
        pole_parol = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT).send_keys(password)
        print("успешно ввели пароль")
        #вводим подтверждающий пароль
        pole_podtvershd_parol = self.browser.find_element(*LoginPageLocators.REGISTER_PODTVERSHD_PASSWORD_INPUT).send_keys(password)
        print("успешно ввели подтверждающий пароль")
        #кликаем на кнопку "Зарегистрироваться"
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        print("успешно нажали Зарегистрироваться")
    