from locators import SignInPageLocators, HomePageLocators, PersonalAccountLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestsProfile:

    def test_transition_to_personal_account_from_the_main_page_using_the_personal_account_button(self, driver, get_login_driver):
        # проверка перехода в личный кабинет с главной страницы по кнопке Личный кабинет
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.personal_account_bttn))
        driver.find_element(*HomePageLocators.personal_account_bttn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAccountLocators.exit_bttn))
        save_bttn_displayed = driver.find_element(*PersonalAccountLocators.saved_bttn).is_displayed()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile' and save_bttn_displayed

    def test_transition_from_personal_area_to_constructor_from_click_constructor_bttn(self, driver, get_login_driver):
        # проверка перехода из личного кабинета в конструктор по клику на кнопку Конструктор
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.personal_account_bttn))
        driver.find_element(*HomePageLocators.personal_account_bttn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAccountLocators.exit_bttn))
        driver.find_element(*HomePageLocators.constructor_bttn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.buns))
        buns_displayed = driver.find_element(*HomePageLocators.buns).is_displayed()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and buns_displayed

    def test_transition_from_personal_account_to_constructor_from_click_logo(self, driver, get_login_driver):
        # проверка перехода из личного кабинета в конструктор по клику на Логотип
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.personal_account_bttn))
        driver.find_element(*HomePageLocators.personal_account_bttn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAccountLocators.exit_bttn))
        driver.find_element(*HomePageLocators.logo_bttn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.buns))
        buns_displayed = driver.find_element(*HomePageLocators.buns).is_displayed()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and buns_displayed

    def test_logout_from_personal_account(self, driver, get_login_driver):
        # проверка выхода из личного кабинета
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.personal_account_bttn))
        driver.find_element(*HomePageLocators.personal_account_bttn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAccountLocators.exit_bttn))
        driver.find_element(*PersonalAccountLocators.exit_bttn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(SignInPageLocators.login_account_bttn))
        login_bttn_displayed = driver.find_element(*SignInPageLocators.login_account_bttn).is_displayed()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login' and login_bttn_displayed