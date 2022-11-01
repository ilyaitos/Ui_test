from selenium.webdriver.common.by import By
from locator import *
from home_page import HomePage
from conftest import logger


class LaunchesPage(HomePage):

    def click_launches_example(self):
        logger.info('Click launches example')
        launches_example = self.driver.find_element(By.XPATH, LocatorsLaunches.LOCATOR_TEST_EXAMPLE)
        launches_example.click()
        logger.info('Launches example is clicked')

    def dashboard_status_passed(self):
        logger.info('Find  dashboard status passed')
        dashboard_status_passed = self.driver.find_element(By.XPATH, LocatorsLaunches.LOCATOR_DASHBOARD_STATUS_PASSED)
        name = dashboard_status_passed.get_attribute("textContent")
        logger.info('Dashboard status passed found')
        return name

    def dashboard_status_failed(self):
        logger.info('Find  dashboard status failed')
        dashboard_status_failed = self.driver.find_element(By.XPATH, LocatorsLaunches.LOCATOR_DASHBOARD_STATUS_FAILED)
        name = dashboard_status_failed.get_attribute("textContent")
        logger.info('Dashboard status failed found')
        return name

    def dashboard_status_skipped(self):
        logger.info('Find dashboard status skipped')
        dashboard_status_skipped = self.driver.find_element(By.XPATH, LocatorsLaunches.LOCATOR_DASHBOARD_STATUS_SKIPPED)
        name = dashboard_status_skipped.get_attribute("textContent")
        logger.info('Dashboard status skipped found')
        return name
