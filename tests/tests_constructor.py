from locators import HomePageLocators

class TestConstructor:

    def test_transition_to_buns(self, driver):
        # проверка перехода к разделу "Булки"
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*HomePageLocators.sauces_bttn).click()
        driver.find_element(*HomePageLocators.bun_bttn).click()
        buns_text = driver.find_element(*HomePageLocators.buns).text

        assert (buns_text == 'Булки') and (driver.find_element(*HomePageLocators.buns_ul).is_displayed()) and 'current' in driver.find_element(*HomePageLocators.buns_class).get_attribute('class')

    def test_transition_to_toppings(self, driver):
        # проверка перехода к разделу "Начинки"
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*HomePageLocators.toppings_bttn).click()
        toppings = driver.find_element(*HomePageLocators.toppings).text

        assert (toppings == 'Начинки') and (driver.find_element(*HomePageLocators.toppings_ul).is_displayed()) and 'current' in driver.find_element(*HomePageLocators.toppings_class).get_attribute('class')

    def test_transitions_to_sauces(self, driver):
        # проверка перехода к разделу "Соусы"
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*HomePageLocators.sauces_bttn).click()
        souces = driver.find_element(*HomePageLocators.sauces).text

        assert (souces == 'Соусы') and (driver.find_element(*HomePageLocators.sauces_ul).is_displayed()) and 'current' in driver.find_element(*HomePageLocators.sauces_class).get_attribute('class')