from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from conftest import logger
from home_page import HomePage
from test import driver
from home_page import LocatorsHomePage


class LocatorsNewDashboard:
    LOCATOR_BUTTON_ADD_NEW_DASHBOARD = '(//button[@class="ghostButton__ghost-button--1PhF7 ghostButton__color-topaz--2GTla with-icon ghostButton__filled-icon--bHBq5 ghostButton__mobile-minified--1m7Pj"])[1]'
    LOCATOR_INPUT_NAME_NEW_DASHBOARD = '//input[@placeholder="Enter dashboard name"]'
    LOCATOR_BUTTON_CONFIRM_ADD_NEW_DASHBOARD = '//button[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]'
    LOCATOR_DELETE_DASHBOARD = '//i[@class="icon__icon--2m6Od icon__icon-delete--1jIHF"]'
    LOCATOR_CONFIRM_DELETE_DASHBOARD = '//button[@class="bigButton__big-button--ivY7j bigButton__color-tomato--Wvy5L"]'
    LOCATOR_DASHBOARD_NAME = '//a[@class="gridCell__grid-cell--3e2mS gridCell__align-left--2beIG dashboardTable__name--1sWJs"]'
    LOCATOR_LIST_DASHBOARD_NAME = '//*[@class="gridRow__grid-row-wrapper--1dI9K"]'
    www = '//*[@class="gridRow__grid-row-wrapper--1dI9K"]//a[text() = "ilya"]'
    www2 = '//*[@class="gridCell__grid-cell--3e2mS gridCell__align-left--2beIG dashboardTable__name--1sWJs"]'
    www3 = '//*[@class="gridRow__grid-row-wrapper--1dI9K"]//a[text() = "ilya"]/..//*[@class="icon__icon--2m6Od icon__icon-delete--1jIHF"]'
    www222 = '//*[@class="gridRow__grid-row--1pS-5"]//*[text() ="ilya"]'


class LocatorsNewWidget:
    LOCATOR_ADD_NEW_WIDGET = '(//button[@class="ghostButton__ghost-button--1PhF7 ghostButton__color-topaz--2GTla with-icon ghostButton__filled-icon--bHBq5 ghostButton__mobile-minified--1m7Pj"])[2]'
    LOCATOR_WIDGET_TYPE_NEXT_STEP = '//div[@class="widgetWizardModal__widget-wizard--fG8kx"]//button[@class="ghostButton__ghost-button--1PhF7 ghostButton__color-topaz--2GTla with-icon ghostButton__filled-icon--bHBq5 ghostButton__mobile-minified--1m7Pj"]'
    LOCATOR_CONFIGURE_WIDGET_FILTER_SDDF = '//div[@class="filtersItem__filter-item--1OosV"]'
    LOCATOR_CONFIGURE_WIDGET_TYPE_NEXT_STEP = '(//div[@class="widgetWizardModal__widget-wizard--fG8kx"]//button[@class="ghostButton__ghost-button--1PhF7 ghostButton__color-topaz--2GTla with-icon ghostButton__filled-icon--bHBq5 ghostButton__mobile-minified--1m7Pj"])[3]'
    LOCATOR_SAVE_ADD = '//button[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]'
    LOCATOR_WIDGET_NAME = '//div[@class="widgetHeader__widget-name-block--7fZoV"][text() = "Dog1"]'
    LOCATOR_INPUT_WIDGET_NAME = '//*[@placeholder="Enter widget name"]'


class LocatorsNameWidget:
    LOCATOR_WIDGET_LAUNCH_STATISTICS_CHART = '//div[@class="widget-type-selector"]//div[text() ="Launch statistics chart"]'
    LOCATOR_WIDGET_OVERALL_STSTISTICS = '//div[@class="widget-type-selector"]//div[text() ="Overall statistics"]'
    LOCATOR_WIDGET_LAUNCHES_DURATION_CHART = '//div[@class="widget-type-selector"]//div[text() ="Launches duration chart"]'
    LOCATOR_WIDGET_LAUNCH_EXECUTION_AND_ISSUE_STATISTIC = '//div[@class="widget-type-selector"]//div[text() ="Launch execution and issue statistic"]'
    LOCATOR_WIDGET_PROJECT_ACTIVITY_PANEL = '//div[@class="widget-type-selector"]//div[text() ="Project activity panel"]'
    LOCATOR_WIDGET_TEST_CASES_GROWTH_TREND_CHART = '//div[@class="widget-type-selector"]//div[text() ="Test-cases growth trend chart"]'
    LOCATOR_WIDGET_INVESTIGATED_PERCENTAGE_OF_LAUNCHES = '//div[@class="widget-type-selector"]//div[text() ="Investigated percentage of launches"]'
    LOCATOR_WIDGET_LAUNCHES_TABLE = '//div[@class="widget-type-selector"]//div[text() ="Launches table"]'
    LOCATOR_WIDGET_UNIQUE_BUGS_TABLE = '//div[@class="widget-type-selector"]//div[text() ="Unique bugs table"]'
    LOCATOR_WIDGET_MOST_FAILED_TEST_CASES_TABLE = '//div[@class="widget-type-selector"]//div[text() ="Most failed test-cases table (TOP-20)"]'
    LOCATOR_WIDGET_FAILED_CASES_TREND_CHART = '//div[@class="widget-type-selector"]//div[text() ="Failed cases trend chart"]'
    LOCATOR_WIDGET_NON_PASSED_TEST_CASES_TREND_CHART = '//div[@class="widget-type-selector"]//div[text() ="Non-passed test-cases trend chart"]'
    LOCATOR_WIDGET_DIFFEREN_LAUNCHES_COMPARISON_CHART = '//div[@class="widget-type-selector"]//div[text() ="Different launches comparison chart"]'
    LOCATOR_WIDGET_PASSING_RATE_PER_LAUNCH = '//div[@class="widget-type-selector"]//div[text() ="Passing rate per launch"]'
    LOCATOR_WIDGET_PASSING_RATE_SUMMARY = '//div[@class="widget-type-selector"]//div[text() ="Passing rate summary"]'
    LOCATOR_WIDGET_FLAKY_TEST_CASES_TABLE = '//div[@class="widget-type-selector"]//div[text() ="Flaky test cases table (TOP-20)"]'
    LOCATOR_WIDGET_CUMULATIVE_TREND_CHART = '//div[@class="widget-type-selector"]//div[text() ="Cumulative trend chart"]'
    LOCATOR_WIDGET_MOST_POPULAR_PATTERN_TABLE = '//div[@class="widget-type-selector"]//div[text() ="Most popular pattern table (TOP-20)"]'
    LOCATOR_WIDGET_COMPONENT_HEALTH_CHECK = '//div[@class="widget-type-selector"]//div[text() ="Component health check"]'
    LOCATOR_WIDGET_COMPONENT_HEALTH_CHECK_TABLE_VIEW = '//div[@class="widget-type-selector"]//div[text() ="Component health check (table view)"]'
    LOCATOR_WIDGET_MOST_TIME_CONSUMING_TEST_CASES_WIDGET = '//div[@class="widget-type-selector"]//div[text() ="Most time-consuming test cases widget (TOP-20)"]'


class LocatorsNameFilter:
    LOCATOR_FILTER_1 = "// *[text() = 'filter_1']"
    LOCATOR_FILTER_2 = "// *[text() = 'filter_2']"
    LOCATOR_FILTER_3 = "// *[text() = 'filter_3']"


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


class NameFilter:
    FILTER_1 = LocatorsNameFilter.LOCATOR_FILTER_1
    FILTER_2 = LocatorsNameFilter.LOCATOR_FILTER_2
    FILTER_3 = LocatorsNameFilter.LOCATOR_FILTER_3









class Dashboard():

    def __init__(self, name_dashboard):
        self.name_dashboard = name_dashboard


#
# def objects_dashboard(self):
#     click_button_add_new_dashboard = driver.find_element(By.XPATH,
#                                                               LocatorsNewDashboard.LOCATOR_BUTTON_ADD_NEW_DASHBOARD)
#     click_button_add_new_dashboard.click()
#     input_name_new_dashboard = driver.find_element(By.XPATH,
#                                                         LocatorsNewDashboard.LOCATOR_INPUT_NAME_NEW_DASHBOARD)
#     input_name_new_dashboard.send_keys(self.name1)
#     click_button_add = driver.find_element(By.XPATH,
#                                                 LocatorsNewDashboard.LOCATOR_BUTTON_CONFIRM_ADD_NEW_DASHBOARD)
#     click_button_add.click()





class ObjectsPage(HomePage):

    def objects_dashboard(self, name):
        click_button_add_new_dashboard = self.driver.find_element(By.XPATH,
                                                                  LocatorsNewDashboard.LOCATOR_BUTTON_ADD_NEW_DASHBOARD)
        click_button_add_new_dashboard.click()
        input_name_new_dashboard = self.driver.find_element(By.XPATH,
                                                            LocatorsNewDashboard.LOCATOR_INPUT_NAME_NEW_DASHBOARD)
        input_name_new_dashboard.send_keys(name)
        click_button_add = self.driver.find_element(By.XPATH,
                                                    LocatorsNewDashboard.LOCATOR_BUTTON_CONFIRM_ADD_NEW_DASHBOARD)
        click_button_add.click()

    def objects_widget(self, dashboard_name, type_widget, name_filter, name_widget):
        lists = []
        click_button_dashboard = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_DASHBOARD)
        click_button_dashboard.click()
        list_name = self.driver.find_elements(By.XPATH, LocatorsNewDashboard.www2)
        for x in list_name:
            lists.append(x.get_attribute("textContent"))
        if dashboard_name in lists:
            click_dashboard_name = self.driver.find_element(By.XPATH, '(//*[@class="gridCell__grid-cell--3e2mS gridCell__align-left--2beIG dashboardTable__name--1sWJs"][text() ="{}"])'.format(dashboard_name))
            click_dashboard_name.click()
            click_button_add_new_widget = self.driver.find_element(By.XPATH, LocatorsNewWidget.LOCATOR_ADD_NEW_WIDGET).click()
            click_button_widget_launch_statistics_chart = self.driver.find_element(By.XPATH, type_widget).click()

            click_button_widget_type_next_step = self.driver.find_element(By.XPATH,
                                                                          LocatorsNewWidget.LOCATOR_WIDGET_TYPE_NEXT_STEP).click()
            click_button_configure_widget_filter = self.driver.find_element(By.XPATH, name_filter).click()
            click_button_configure_widget_type_next_step = self.driver.find_element(By.XPATH,
                                                                                    LocatorsNewWidget.LOCATOR_CONFIGURE_WIDGET_TYPE_NEXT_STEP).send_keys(Keys.ENTER)
            input_widget_name = self.driver.find_element(By.XPATH, LocatorsNewWidget.LOCATOR_INPUT_WIDGET_NAME)
            input_widget_name.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
            input_widget_name.send_keys(name_widget)
            click_button_save_add = self.driver.find_element(By.XPATH, LocatorsNewWidget.LOCATOR_SAVE_ADD).click()

    def objects_delete_dashboard(self, list_dashboard_name):
        lists = []
        click_button_dashboard = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_DASHBOARD)
        click_button_dashboard.click()
        list_name = self.driver.find_elements(By.XPATH, LocatorsNewDashboard.www2)
        for x in list_name:
            lists.append(x.get_attribute("textContent"))
        for x in lists:
            for e in list_dashboard_name:
                if x == e:
                    click_button_dashboard = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_DASHBOARD)
                    click_button_dashboard.click()
                    click_button_delete_dashboard = self.driver.find_element(By.XPATH, '//*[@class="gridRow__grid-row-wrapper--1dI9K"]//a[text() ="{}"]/..//*[@class="icon__icon--2m6Od icon__icon-delete--1jIHF"]'.format(e))
                    click_button_delete_dashboard.click()
                    click_button_confirm_delete_dashboard = self.driver.find_element(By.XPATH, LocatorsNewDashboard.LOCATOR_CONFIRM_DELETE_DASHBOARD)#+str(e)+
                    click_button_confirm_delete_dashboard.click()


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

    def search_dashboard_with_name(self, name):
        logger.info('Find dashboard name')
        lists = []
        dashboard_name = self.driver.find_elements(By.XPATH, LocatorsNewDashboard.LOCATOR_DASHBOARD_NAME)
        for x in dashboard_name:
            if x.get_attribute("textContent") == name:
                return name
        logger.info('Find dashboard found')

    def widget_name(self):
        logger.info('Find widget name')
        widget_name = self.driver.find_element(By.XPATH, LocatorsNewWidget.LOCATOR_WIDGET_NAME)
        name = widget_name.get_attribute("textContent")
        logger.info('Widget name found')
        return name

    def click_button_add_new_dashboard(self):
        logger.info('Click dashboard button')
        click_button_add_new_dashboard = self.driver.find_element(By.XPATH,
                                                                  LocatorsNewDashboard.LOCATOR_BUTTON_ADD_NEW_DASHBOARD)
        click_button_add_new_dashboard.click()
        logger.info('Dashboard button is clicked')

    def input_name_dashboard(self, name):
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

    def click_button_configure_widget_filter(self, name_filter):
        logger.info('Click widget filter sddf button')
        click_button_configure_widget_filter_sddf = self.driver.find_element(By.XPATH, name_filter)
        click_button_configure_widget_filter_sddf.click()
        logger.info('Widget filter sddf button is clicked')

    def input_widget_name(self, name_widget):
        logger.info('Click widget filter sddf button')
        input_widget_name = self.driver.find_element(By.XPATH, LocatorsNewWidget.LOCATOR_INPUT_WIDGET_NAME)
        input_widget_name.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        input_widget_name.send_keys(name_widget)
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
