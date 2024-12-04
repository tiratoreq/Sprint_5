from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver, login
from locators import Locators

class TestConstructor:
    def test_goto_boolochli(self, driver, login):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SOUSES)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BOOLOCHKI)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BOOLKA_IN_MENU))

    def test_goto_sousi(self, driver, login):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SOUSES)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SOUS_IN_MENU))

    def test_goto_nachinki(self, driver, login):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.NACHINKI)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.NACHINKA_IN_MENU))
