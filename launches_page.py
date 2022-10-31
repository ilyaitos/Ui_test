from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from locator import *
from conftest import logger
from home_page import HomePage


class LaunchesPage(HomePage):

    def click_launches_example(self):
        launches_example = self.driver.find_elements(By.XPATH, LocatorsLaunches.LOCATOR_TEST_EXAMPLE)
        launches_example.click()

    def dashboard_status_passed(self):
        dashboard_status_passed = self.driver.find_elements(By.XPATH, LocatorsLaunches.LOCATOR_DASHBOARD_STATUS_PASSED)
        dashboard_status_passed.get_attribute("textContent")
