from selenium.webdriver.common.by import By
from conftest import logger, driver


class LocatorsHomePage:
    LOCATOR_BUTTON_DASHBOARD = '(//a[@href="#default_personal/dashboard"])[1]'
    LOCATOR_BUTTON_LAUNCHES = '//a[@href="#default_personal/launches_page"]'
    LOCATOR_BUTTON_FILTERS = '//a[@href="#default_personal/filters"]'
    LOCATOR_BUTTON_DEBUG = '//a[@href="#default_personal/userdebug/all"]'
    LOCATOR_BUTTON_PROJECT_MEMBERS = '//a[@href="#default_personal/members"]'
    LOCATOR_BUTTON_PROJECT_SETTINGS = '//a[@href="#default_personal/settings"]'
    LOCATOR_BUTTON_DEFAULT_DROP = '(//*[@class="userBlock__avatar-wrapper--_Jkks"])[1]'
    LOCATOR_BUTTON_PROFILE = '(//a[contains(@href,"#user-profile_page")])[2]'
    LOCATOR_BUTTON_LOGOUT = '//div[@class="userBlock__menu-item--3VBsZ"]'


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_button_dashboard(self):
        logger.info('Click dashboard button')
        click_button_dashboard = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_DASHBOARD)
        click_button_dashboard.click()
        logger.info('Dashboard button is clicked')

    def click_button_launches(self):
        logger.info('Click launches_page button')
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
        driver.refresh()
        click_button_default_drop = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_DEFAULT_DROP)
        click_button_default_drop.click()
        logger.info('Default drop button is clicked')

    def click_button_profile(self):
        logger.info('Click profile_page button')
        click_button_profile = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_PROFILE)
        click_button_profile.click()
        logger.info('Profile button is clicked')

    def click_button_logout(self):
        logger.info('Click logout button')
        click_button_logout = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_LOGOUT)
        click_button_logout.click()
        logger.info('Logout button is clicked')

    def current_url(self):
        logger.info('Find current url')
        current_url = self.driver.current_url
        logger.info('Current url found')
        return current_url
