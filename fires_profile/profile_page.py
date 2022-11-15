from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from conftest import logger
from home_page import HomePage


class LocatorsProfile:
    LOCATOR_EDITING_NICKNAM = '//span[@class="userInfo__pencil-icon--2WZhA"]'
    LOCATOR_USER_NAME = '//input[ @ placeholder = "Enter user name"]'
    LOCATOR_SUBMIT = '//button[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]'
    LOCATOR_USER_NAME_ON_THE_PAGE = '//span[@class="userInfo__name--1aIPl"]'


class ProfilePage(HomePage):

    def click_button_editing_nickname(self):
        logger.info('Click editing nickname button')
        click_button_editing_nickname = self.driver.find_element(By.XPATH, LocatorsProfile.LOCATOR_EDITING_NICKNAM)
        click_button_editing_nickname.click()
        logger.info('Editing nickname button is clicked')

    def input_user_name(self, name):
        logger.info('Enter user name')
        input_user_name = self.driver.find_element(By.XPATH, LocatorsProfile.LOCATOR_USER_NAME)
        input_user_name.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        input_user_name.send_keys(name)
        logger.info('User name accepted')

    def user_name(self):
        logger.info('Find name user ')
        user_name = self.driver.find_element(By.XPATH, LocatorsProfile.LOCATOR_USER_NAME_ON_THE_PAGE)
        name = user_name.get_attribute("textContent")
        logger.info('Name user found')
        return name

    def click_button_submit(self):
        logger.info('Click submit button')
        click_button_submit = self.driver.find_element(By.XPATH, LocatorsProfile.LOCATOR_SUBMIT)
        click_button_submit.click()
        logger.info('Submit button is clicked')
