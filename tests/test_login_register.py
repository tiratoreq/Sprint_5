from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from faker import Faker

from conftest import driver
from constants import Constants
from locators import Locators

faker = Faker()

class TestSBLoginRegister:

    @staticmethod
    def registration(driver):
        email = faker.email()
        driver.find_element(*Locators.LK).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(Constants.NAME)
        driver.find_element(*Locators.EMAIL).send_keys(email)

    def test_registration(self, driver):
        self.registration(driver)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AUTH_BUTTON))

    def test_registration_wrong_password(self, driver):
        self.registration(driver)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.WRONG_PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        assert driver.find_element(*Locators.PASSWORD_MESS)

    @staticmethod
    def login_form_fill(driver):
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

    def test_login_via_account_button(self, driver, login):
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER))

    def test_login_via_lk_button(self, driver):
        driver.find_element(*Locators.LK).click()
        self.login_form_fill(driver)
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER))

    def test_login_via_register_page(self, driver):
        driver.find_element(*Locators.LK).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.ENTER_LINK).click()
        self.login_form_fill(driver)
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER))

    def test_login_via_reset_password_page(self, driver):
        driver.find_element(*Locators.LK).click()
        driver.find_element(*Locators.PASSWORD_RESET).click()
        driver.find_element(*Locators.ENTER_LINK).click()
        self.login_form_fill(driver)
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER))