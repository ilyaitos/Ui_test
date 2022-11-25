from selenium.webdriver.common.by import By
from home_page import HomePage
from conftest import logger


class LocatorsRegistrationPage:
    LOCATOR_LOGIN_FIELD = "//*[@class='inputOutside__input--1Sg9p'][@type='text']"
    LOCATOR_PASSWORD_FIELD = "//*[@class='inputOutside__input--1Sg9p'][@type='password']"
    LOCATOR_BUTTON_TO_COME_IN = '//*[@type="submit"]'


class RegistrationPage(HomePage):

    def input_login(self, login):
        logger.info('Enter login')
        input_login = self.driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_LOGIN_FIELD)
        input_login.send_keys(login)
        logger.info('Login accepted')

    def input_password(self, password):
        logger.info('Enter password')
        input_password = self.driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_PASSWORD_FIELD)
        input_password.send_keys(password)
        logger.info('Password accepted')

    def click_button_login(self):
        logger.info('Click login button')
        click_button_login = self.driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_BUTTON_TO_COME_IN)
        click_button_login.click()
        logger.info('Login button is clicked')

    def current_url(self):
        logger.info('Find current url')
        current_url = self.driver.current_url
        logger.info('Current url found')
        return current_url
