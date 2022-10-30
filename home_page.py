from selenium.webdriver.common.by import By
from locator import *
from conftest import logger


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def current_url(self):
        current_url = self.driver.current_url
        return current_url

    def input_login(self, login):
        input_login = self.driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_LOGIN_FIELD)
        input_login.send_keys(login)

    def input_password(self, password):
        input_password = self.driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_PASSWORD_FIELD)
        input_password.send_keys(password)

    def click_button_login(self):
        logger.info('Click login button')
        click_button_login = self.driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_BUTTON_TO_COME_IN)
        click_button_login.click()
        logger.info('Login button is clicked')

    def click_button_dashboard(self):
        logger.info('Click dashboard button')
        click_button_dashboard = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_DASHBOARD)
        click_button_dashboard.click()
        logger.info('Dashboard button is clicked')

    def click_button_launches(self):
        logger.info('Click launches button')
        click_button_launches = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_LAUNCHES)
        click_button_launches.click()
        logger.info('Launches button is clicked')

    def click_button_filters(self):
        logger.info('Click filters button')
        click_button_filters = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_FILTERS)
        click_button_filters.click()
        logger.info('Filters button is clicked')

    def click_button_debug(self):
        logger.info('Click debug button')
        click_button_debug = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_DEBUG)
        click_button_debug.click()
        logger.info('Debug button is clicked')

    def click_button_project_members(self):
        logger.info('Click project members button')
        click_button_project_members = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_PROJECT_MEMBERS)
        click_button_project_members.click()
        logger.info('Project members button is clicked')

    def click_button_project_settings(self):
        logger.info('Click project settings button')
        click_button_project_settings = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_PROJECT_SETTINGS)
        click_button_project_settings.click()
        logger.info('Project settings button is clicked')

    def click_button_default_drop(self):
        logger.info('Click default drop button')
        click_button_default_drop = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_DEFAULT_DROP)
        click_button_default_drop.click()
        logger.info('Default drop button is clicked')

    def click_button_profile(self):
        logger.info('Click profile button')
        click_button_profile = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_PROFILE)
        click_button_profile.click()
        logger.info('Profile button is clicked')

    def click_button_logout(self):
        logger.info('Click logout button')
        click_button_logout = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_LOGOUT)
        click_button_logout.click()
        logger.info('Logout button is clicked')
