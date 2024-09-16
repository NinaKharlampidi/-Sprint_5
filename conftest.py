from selenium import webdriver
import pytest
from faker import Faker

fake = Faker()

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def unique_email():
    return fake.email()

@pytest.fixture
def user_data():
    return {'username': fake.user_name(), 'password': fake.password()}