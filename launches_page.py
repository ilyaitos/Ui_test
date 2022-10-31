from selenium.webdriver.common.by import By
from locator import *
from home_page import HomePage


class LaunchesPage(HomePage):

    def click_launches_example(self):
        launches_example = self.driver.find_element(By.XPATH, LocatorsLaunches.LOCATOR_TEST_EXAMPLE)
        launches_example.click()

    def dashboard_status_passed(self):
        dashboard_status_passed = self.driver.find_element(By.XPATH, LocatorsLaunches.LOCATOR_DASHBOARD_STATUS_PASSED)
        name = dashboard_status_passed.get_attribute("textContent")
        return name

    def dashboard_status_failed(self):
        dashboard_status_failed = self.driver.find_element(By.XPATH, LocatorsLaunches.LOCATOR_DASHBOARD_STATUS_FAILED)
        name = dashboard_status_failed.get_attribute("textContent")
        return name

    def dashboard_status_skipped(self):
        dashboard_status_skipped = self.driver.find_element(By.XPATH, LocatorsLaunches.LOCATOR_DASHBOARD_STATUS_SKIPPED)
        name = dashboard_status_skipped.get_attribute("textContent")
        return name
