from locators import HomePageLocators

class TestConstructor:

    def test_transition_to_buns(self, driver):
        # проверка перехода к разделу "Булки"
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*HomePageLocators.sauces_bttn).click()
        driver.find_element(*HomePageLocators.bun_bttn).click()
        buns_text = driver.find_element(*HomePageLocators.buns).text
        buns_displayed = driver.find_element(*HomePageLocators.buns_ul).is_displayed()

        assert buns_text == 'Булки' and buns_displayed

    def test_transition_to_toppings(self, driver):
        # проверка перехода к разделу "Начинки"
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*HomePageLocators.toppings_bttn).click()
        toppings = driver.find_element(*HomePageLocators.toppings).text
        toppings_displayed = driver.find_element(*HomePageLocators.toppings_ul).is_displayed()

        assert toppings == 'Начинки' and toppings_displayed

    def test_transitions_to_sauces(self, driver):
        # проверка перехода к разделу "Соусы"
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*HomePageLocators.sauces_bttn).click()
        souces = driver.find_element(*HomePageLocators.sauces).text
        souces_displayed = driver.find_element(*HomePageLocators.sauces_ul).is_displayed()

        assert souces == 'Соусы' and souces_displayed