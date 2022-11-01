from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from locator import *
from conftest import logger
from home_page import HomePage


class NameWidget:
    LAUNCH_STATISTICS_CHART = LocatorsNameWidget.LOCATOR_WIDGET_LAUNCH_STATISTICS_CHART
    OVERALL_STSTISTICS = LocatorsNameWidget.LOCATOR_WIDGET_OVERALL_STSTISTICS
    LAUNCHES_DURATION_CHART = LocatorsNameWidget.LOCATOR_WIDGET_LAUNCHES_DURATION_CHART
    LAUNCH_EXECUTION_AND_ISSUE_STATISTIC = LocatorsNameWidget.LOCATOR_WIDGET_LAUNCH_EXECUTION_AND_ISSUE_STATISTIC
    PROJECT_ACTIVITY_PANEL = LocatorsNameWidget.LOCATOR_WIDGET_PROJECT_ACTIVITY_PANEL
    TEST_CASES_GROWTH_TREND_CHART = LocatorsNameWidget.LOCATOR_WIDGET_TEST_CASES_GROWTH_TREND_CHART
    INVESTIGATED_PERCENTAGE_OF_LAUNCHES = LocatorsNameWidget.LOCATOR_WIDGET_INVESTIGATED_PERCENTAGE_OF_LAUNCHES
    LAUNCHES_TABLE = LocatorsNameWidget.LOCATOR_WIDGET_LAUNCHES_TABLE
    UNIQUE_BUGS_TABLE = LocatorsNameWidget.LOCATOR_WIDGET_UNIQUE_BUGS_TABLE
    MOST_FAILED_TEST_CASES_TABLE = LocatorsNameWidget.LOCATOR_WIDGET_MOST_FAILED_TEST_CASES_TABLE
    FAILED_CASES_TREND_CHART = LocatorsNameWidget.LOCATOR_WIDGET_FAILED_CASES_TREND_CHART
    NON_PASSED_TEST_CASES_TREND_CHART = LocatorsNameWidget.LOCATOR_WIDGET_NON_PASSED_TEST_CASES_TREND_CHART
    DIFFEREN_LAUNCHES_COMPARISON_CHART = LocatorsNameWidget.LOCATOR_WIDGET_DIFFEREN_LAUNCHES_COMPARISON_CHART
    PASSING_RATE_PER_LAUNCH = LocatorsNameWidget.LOCATOR_WIDGET_PASSING_RATE_PER_LAUNCH
    PASSING_RATE_SUMMARY = LocatorsNameWidget.LOCATOR_WIDGET_PASSING_RATE_SUMMARY
    FLAKY_TEST_CASES_TABLE = LocatorsNameWidget.LOCATOR_WIDGET_FLAKY_TEST_CASES_TABLE
    CUMULATIVE_TREND_CHART = LocatorsNameWidget.LOCATOR_WIDGET_CUMULATIVE_TREND_CHART
    MOST_POPULAR_PATTERN_TABLE = LocatorsNameWidget.LOCATOR_WIDGET_MOST_POPULAR_PATTERN_TABLE
    COMPONENT_HEALTH_CHECK = LocatorsNameWidget.LOCATOR_WIDGET_COMPONENT_HEALTH_CHECK
    COMPONENT_HEALTH_CHECK_TABLE_VIEW = LocatorsNameWidget.LOCATOR_WIDGET_COMPONENT_HEALTH_CHECK_TABLE_VIEW
    MOST_TIME_CONSUMING_TEST_CASES_WIDGET = LocatorsNameWidget.LOCATOR_WIDGET_MOST_TIME_CONSUMING_TEST_CASES_WIDGET


class DashboardPage(HomePage):

    def click_button_widget_launch_statistics_chart(self, name):
        logger.info('Click widget launch statistics chart button')
        click_button_widget_launch_statistics_chart = self.driver.find_element(By.XPATH, name)
        click_button_widget_launch_statistics_chart.click()
        logger.info('Widget launch statistics chart button is clicked')

    def list_dashboard_name(self):
        logger.info('Find list dashboard name')
        list_dashboard_name = self.driver.find_elements(By.XPATH, LocatorsNewDashboard.LOCATOR_LIST_DASHBOARD_NAME)
        logger.info('List dashboard name found')
        return list_dashboard_name

    def dashboard_name(self):
        logger.info('Find dashboard name')
        lists = []
        dashboard_name = self.driver.find_elements(By.XPATH, LocatorsNewDashboard.LOCATOR_DASHBOARD_NAME)
        for x in dashboard_name:
            lists.append(x.get_attribute("textContent"))
        logger.info('Find dashboard found')
        return lists

    def widget_name(self):
        logger.info('Find widget name')
        self.driver.find_elements(By.XPATH, LocatorsNewWidget.LOCATOR_WIDGET_NAME)
        logger.info('Widget name found')

    def click_button_add_new_dashboard(self):
        logger.info('Click dashboard button')
        click_button_add_new_dashboard = self.driver.find_element(By.XPATH,
                                                                  LocatorsNewDashboard.LOCATOR_BUTTON_ADD_NEW_DASHBOARD)
        click_button_add_new_dashboard.click()
        logger.info('Dashboard button is clicked')

    def input_name_new_dashboard(self, name):
        logger.info('Enter name')
        input_name_new_dashboard = self.driver.find_element(By.XPATH,
                                                            LocatorsNewDashboard.LOCATOR_INPUT_NAME_NEW_DASHBOARD)
        input_name_new_dashboard.send_keys(name)
        logger.info('Name accepted')

    def click_button_add(self):
        logger.info('Click add button')
        click_button_add = self.driver.find_element(By.XPATH, LocatorsNewDashboard.LOCATOR_BUTTON_CONFIRM_ADD_NEW_DASHBOARD)
        click_button_add.click()
        logger.info('Add button is clicked')

    def click_button_delete_dashboard(self):
        logger.info('Click delete dashboard button')
        click_button_delete_dashboard = self.driver.find_element(By.XPATH,
                                                                 LocatorsNewDashboard.LOCATOR_DELETE_DASHBOARD)
        click_button_delete_dashboard.click()
        logger.info('Delete dashboard button is clicked')

    def click_button_confirm_delete_dashboard(self):
        logger.info('Confirm delete dashboard')
        click_button_confirm_delete_dashboard = self.driver.find_element(By.XPATH,
                                                                         LocatorsNewDashboard.LOCATOR_CONFIRM_DELETE_DASHBOARD)
        click_button_confirm_delete_dashboard.click()
        logger.info('Confirmed dashboard deletion')

    def click_button_add_new_widget(self):
        logger.info('Click add new widget button')
        click_button_add_new_widget = self.driver.find_element(By.XPATH, LocatorsNewWidget.LOCATOR_ADD_NEW_WIDGET)
        click_button_add_new_widget.click()
        logger.info('Add new widget dashboard button is clicked')

    def click_dashboard_name(self):
        logger.info('Click dashboard name ')
        click_dashboard_name = self.driver.find_element(By.XPATH, LocatorsNewDashboard.LOCATOR_DASHBOARD_NAME)
        click_dashboard_name.click()
        logger.info('Dashboard name is clicked')

    def click_button_widget_type_next_step(self):
        logger.info('Click next step button')
        click_button_widget_type_next_step = self.driver.find_element(By.XPATH,
                                                                      LocatorsNewWidget.LOCATOR_WIDGET_TYPE_NEXT_STEP)
        click_button_widget_type_next_step.click()
        logger.info('Next step button is clicked')

    def click_button_configure_widget_filter_sddf(self):
        logger.info('Click widget filter sddf button')
        click_button_configure_widget_filter_sddf = self.driver.find_element(By.XPATH,
                                                                             LocatorsNewWidget.LOCATOR_CONFIGURE_WIDGET_FILTER_SDDF)
        click_button_configure_widget_filter_sddf.click()
        logger.info('Widget filter sddf button is clicked')

    def click_button_configure_widget_type_next_step(self):
        logger.info('Click next step button')
        click_button_configure_widget_type_next_step = self.driver.find_element(By.XPATH,
                                                                                LocatorsNewWidget.LOCATOR_CONFIGURE_WIDGET_TYPE_NEXT_STEP)
        click_button_configure_widget_type_next_step.send_keys(Keys.ENTER)
        logger.info('Next step button is clicked')

    def click_button_save_add(self):
        logger.info('Click add button')
        click_button_save_add = self.driver.find_element(By.XPATH, LocatorsNewWidget.LOCATOR_SAVE_ADD)
        click_button_save_add.click()
        logger.info('Add button is clicked')
