from selenium.webdriver.common.by import By


class HomePageLocators:
    # локаторы главной страницы и конструктора
    home_form = (By.XPATH, ".//main[@class = 'App_componentContainer__2JC2W']")  # форма главной страницы сайта
    logo_bttn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # кнопка главной страницы сайта
    account_login_bttn = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # кнопка войти в аккаунт
    personal_account_bttn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # кнопка личного кабинета
    constructor_bttn = (By.XPATH, ".//p[text() = 'Конструктор']")  # кнопка конструктор
    order_feed_bttn = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # кнопка лента заказов
    bun_bttn = (By.XPATH, ".//span[text() = 'Булки']")  # кнопка переключения на булки
    sauces_bttn = (By.XPATH, ".//span[text() = 'Соусы']")  # кнопка переключения на соусы
    toppings_bttn = (By.XPATH, ".//span[text() = 'Начинки']")  # кнопка переключения на начинки
    place_order_bttn = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # кнопка оформить заказ
    buns = (By.XPATH, ".//h2[text() = 'Булки']")  # текст булки на главной странице
    buns_ul = (
        By.XPATH,
        "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[1]")  # выбор булок на главной странице
    toppings = (By.XPATH, ".//h2[text() = 'Начинки']")  # текст начинки на главной странице
    toppings_ul = (
        By.XPATH,
        "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[3]")  # выбор начинок на главной странице
    sauces = (By.XPATH, ".//h2[text() = 'Соусы']")  # текст соусы на главной странице
    sauces_ul = (
        By.XPATH,
        "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[2]")  # выбор соусов на главной странице
    # локаторы активных вкладок Булок, Соусов и Начинок
    buns_class = (By.XPATH, ".//span[text()='Булки']/ancestor::div[contains(@class, 'current')]")
    sauces_class = (By.XPATH, ".//span[text()='Соусы']/ancestor::div[contains(@class, 'current')]")
    toppings_class = (By.XPATH, ".//span[text()='Начинки']/ancestor::div[contains(@class, 'current')]")

class SignInPageLocators:
    # локаторы авторизации пользователя
    auth_form = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")  # форма авторизации
    email_input = (By.XPATH, ".//input[@name = 'name']")  # поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")  # поле ввода пароля
    registration_bttn = (By.XPATH, "//a[text() = 'Зарегистрироваться']")  # кнопка зерегистрироваться
    login_account_bttn = (By.XPATH, "//button[text() = 'Войти']")  # кнопка войти
    reset_bttn = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # кнопка восстановления пароля


class RegistrationFormLocators:
    # локаторы страницы регистрации
    name_input = (By.XPATH, "(.//input[@name = 'name'])[1]")  # поле ввода имени
    email_input = (By.XPATH, "(.//input[@name = 'name'])[2]")  # поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")  # поле ввода пароля
    error_message_double_reg = (
        By.XPATH, ".//p[text() = 'Такой пользователь уже существует']")  # ошибка при повторной регистрации
    error_message_incorrect_password = (
        By.XPATH, ".//p[text() = 'Некорректный пароль']")  # ошибка при вводе некорректного пароля


class PersonalAccountLocators:
    # локаторы личного кабинета пользователя
    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")  # форма личного кабинета
    profile_bttn = (By.XPATH, ".//a[text() = 'Профиль']")  # кнопка профиль
    order_history_bttn = (By.XPATH, ".//a[text() = 'История заказов']")  # кнопка история заказов
    saved_bttn = (By.XPATH, ".//button[text() = 'Сохранить']")  # кнопка сохранить
    cansel_bttn = (By.XPATH, ".//button[text() = 'Отмена']")  # кнопка отмена
    exit_bttn = (By.XPATH, ".//button[text() = 'Выход']")  # кнопка выход

class PasswordResetLocators:
    # локаторы страницы восстановления пароля пользователя
    email_input = (By.XPATH, ".//label[text() = 'Email']")  # поле ввода email
    reset_bttn = (By.XPATH, ".//button[text() = 'Восстановить']")  # кнопка восстановить

