from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



from conftest import driver, login
from locators import Locators

class TestLKActions:
    def test_lk_redirect(self, driver, login):
        driver.find_element(*Locators.LK).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LK_TEXT))

    def test_constructor_redirect(self,driver, login):
        driver.find_element(*Locators.LK).click()
        driver.find_element(*Locators.CONSTRUCTOR).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER))

    def test_constructor_redirect_via_picture(self, driver, login):
        driver.find_element(*Locators.LK).click()
        driver.find_element(*Locators.PICTURE).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER))

    def test_logout(self, driver,login):
        driver.find_element(*Locators.LK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AUTH_BUTTON))

