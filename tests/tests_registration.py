from data import User
from locators import RegistrationFormLocators, SignInPageLocators
from urls import URLS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationForm:

    def test_registration_success(self, driver, unique_email, user_data):
        # проверка регистрации пользователя
        driver = driver
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(SignInPageLocators.registration_bttn))
        driver.find_element(*RegistrationFormLocators.name_input).send_keys(user_data['username'])
        driver.find_element(*RegistrationFormLocators.email_input).send_keys(unique_email)
        driver.find_element(*RegistrationFormLocators.password_input).send_keys(user_data['password'])
        driver.find_element(*SignInPageLocators.registration_bttn).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(SignInPageLocators.login_account_bttn))
        login_bttn_displayed = driver.find_element(*SignInPageLocators.login_account_bttn).is_displayed()

        assert driver.current_url == URLS.SIGN_PAGE_URL and login_bttn_displayed

    def test_double_registration_check_error(self, driver):
        # проверка повторной регистрации пользователя
        driver = driver
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(SignInPageLocators.registration_bttn))
        driver.find_element(*RegistrationFormLocators.name_input).send_keys(User.user_name)
        driver.find_element(*RegistrationFormLocators.email_input).send_keys(User.email)
        driver.find_element(*RegistrationFormLocators.password_input).send_keys(User.password)
        driver.find_element(*SignInPageLocators.registration_bttn).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(RegistrationFormLocators.error_message_double_reg))
        error = driver.find_element(*RegistrationFormLocators.error_message_double_reg).text

        assert (error == 'Такой пользователь уже существует') and (driver.current_url == URLS.REGA_PAGE_URL)

    def test_registration_incorrect_password_check_error(self, driver):
        # проверка регистрации пользователя с некорректным паролем (менее 6 символов)
        driver = driver
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(SignInPageLocators.registration_bttn))
        driver.find_element(*RegistrationFormLocators.name_input).send_keys(User.user_name)
        driver.find_element(*RegistrationFormLocators.email_input).send_keys(User.email)
        driver.find_element(*RegistrationFormLocators.password_input).send_keys(12345)
        driver.find_element(*SignInPageLocators.registration_bttn).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_any_elements_located(RegistrationFormLocators.error_message_incorrect_password))
        error = driver.find_element(*RegistrationFormLocators.error_message_incorrect_password).text

        assert (error == 'Некорректный пароль') and (driver.current_url == URLS.REGA_PAGE_URL)



