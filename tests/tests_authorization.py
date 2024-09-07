from data import User
from locators import HomePageLocators, SignInPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_login_from_login_bttn(self, driver):
        # вход в личный кабинет через кнопку Войти в аккаунт на главной странице
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*SignInPageLocators.login_account_bttn).click()
        driver.find_element(*SignInPageLocators.email_input).send_keys(User.email)
        driver.find_element(*SignInPageLocators.password_input).send_keys(User.password)
        driver.find_element(*SignInPageLocators.login_account_bttn).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.place_order_bttn))
        order_bttn = driver.find_element(*HomePageLocators.place_order_bttn).text

        assert (driver.current_url == 'https://stellarburgers.nomoreparties.site/') and (order_bttn == 'Оформить заказ')

    def test_login_in_personal_account_from_bttn(self, driver):
        # вход в личный кабинет через кнопку Личный кабинет на главной странице
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*HomePageLocators.personal_account_bttn).click()
        driver.find_element(*SignInPageLocators.email_input).send_keys(User.email)
        driver.find_element(*SignInPageLocators.password_input).send_keys(User.password)
        driver.find_element(*SignInPageLocators.login_account_bttn).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.place_order_bttn))
        order_bttn = driver.find_element(*HomePageLocators.place_order_bttn).text

        assert (driver.current_url == 'https://stellarburgers.nomoreparties.site/') and (order_bttn == 'Оформить заказ')

    def test_login_from_registration_form(self, driver):
        # вход в личный кабинет через форму регистрации
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*SignInPageLocators.login_account_bttn).click()
        driver.find_element(*SignInPageLocators.email_input).send_keys(User.email)
        driver.find_element(*SignInPageLocators.password_input).send_keys(User.password)
        driver.find_element(*SignInPageLocators.login_account_bttn).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.place_order_bttn))
        order_bttn = driver.find_element(*HomePageLocators.place_order_bttn).text

        assert (driver.current_url == 'https://stellarburgers.nomoreparties.site/') and (order_bttn == 'Оформить заказ')

    def test_login_in_reset_form(self, driver):
        # вход в личный кабинет через форму восстановления
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*SignInPageLocators.login_account_bttn).click()
        driver.find_element(*SignInPageLocators.email_input).send_keys(User.email)
        driver.find_element(*SignInPageLocators.password_input).send_keys(User.password)
        driver.find_element(*SignInPageLocators.login_account_bttn).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.place_order_bttn))
        order_bttn = driver.find_element(*HomePageLocators.place_order_bttn).text

        assert (driver.current_url == 'https://stellarburgers.nomoreparties.site/') and (order_bttn == 'Оформить заказ')