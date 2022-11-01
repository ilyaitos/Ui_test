from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from locator import *
from conftest import logger
from home_page import HomePage


class DashboardPage(HomePage):

    def list_dashboard_name(self):
        list_dashboard_name = self.driver.find_elements(By.XPATH, LocatorsNewDashboard.LOCATOR_LIST_DASHBOARD_NAME)
        return list_dashboard_name

    def dashboard_name(self):
        lists = []
        dashboard_name = self.driver.find_elements(By.XPATH, LocatorsNewDashboard.LOCATOR_DASHBOARD_NAME)
        for x in dashboard_name:
            lists.append(x.get_attribute("textContent"))
        return lists

    def widget_name(self):
        widget_name = self.driver.find_elements(By.XPATH, LocatorsNewWidget.LOCATOR_WIDGET_NAME)

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

    def click_button_widget_launch_statistics_chart(self):
        logger.info('Click widget launch statistics chart button')
        click_button_widget_launch_statistics_chart = self.driver.find_element(By.XPATH,
                                                                               LocatorsNewWidget.LOCATOR_WIDGET_LAUNCH_STATISTICS_CHART)
        click_button_widget_launch_statistics_chart.click()
        logger.info('Widget launch statistics chart button is clicked')

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


