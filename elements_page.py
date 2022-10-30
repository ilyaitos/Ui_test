# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from locator import *
# from conftest import logger


# class ElementsPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_button_login(self):
#         logger.info('Click login button')
#         click_button_login = self.driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_BUTTON_TO_COME_IN)
#         click_button_login.click()
#         logger.info('Login button is clicked')
#
#     def click_button_dashboard(self):
#         logger.info('Click dashboard button')
#         click_button_dashboard = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_DASHBOARD)
#         click_button_dashboard.click()
#         logger.info('Dashboard button is clicked')
#
#     def click_button_launches(self):
#         logger.info('Click launches button')
#         click_button_launches = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_LAUNCHES)
#         click_button_launches.click()
#         logger.info('Launches button is clicked')
#
#     def click_button_filters(self):
#         logger.info('Click filters button')
#         click_button_filters = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_FILTERS)
#         click_button_filters.click()
#         logger.info('Filters button is clicked')
#
#     def click_button_debug(self):
#         logger.info('Click debug button')
#         click_button_debug = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_DEBUG)
#         click_button_debug.click()
#         logger.info('Debug button is clicked')
#
#     def click_button_project_members(self):
#         logger.info('Click project members button')
#         click_button_project_members = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_PROJECT_MEMBERS)
#         click_button_project_members.click()
#         logger.info('Project members button is clicked')
#
#     def click_button_project_settings(self):
#         logger.info('Click project settings button')
#         click_button_project_settings = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_PROJECT_SETTINGS)
#         click_button_project_settings.click()
#         logger.info('Project settings button is clicked')
#
#     def click_button_default_drop(self):
#         logger.info('Click default drop button')
#         click_button_default_drop = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_DEFAULT_DROP)
#         click_button_default_drop.click()
#         logger.info('Default drop button is clicked')
#
#     def click_button_profile(self):
#         logger.info('Click profile button')
#         click_button_profile = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_PROFILE)
#         click_button_profile.click()
#         logger.info('Profile button is clicked')
#
#     def click_button_logout(self):
#         logger.info('Click logout button')
#         click_button_logout = self.driver.find_element(By.XPATH, LocatorsHomePage.LOCATOR_BUTTON_LOGOUT)
#         click_button_logout.click()
#         logger.info('Logout button is clicked')

    # def click_button_add_new_dashboard(self):
    #     logger.info('Click dashboard button')
    #     click_button_add_new_dashboard = self.driver.find_element(By.XPATH,
    #                                                               LocatorsNewDashboard.LOCATOR_BUTTON_ADD_NEW_DASHBOARD)
    #     click_button_add_new_dashboard.click()
    #     logger.info('Dashboard button is clicked')
    #
    # def input_name_new_dashboard(self, name):
    #     logger.info('Enter name')
    #     input_name_new_dashboard = self.driver.find_element(By.XPATH,
    #                                                         LocatorsNewDashboard.LOCATOR_INPUT_NAME_NEW_DASHBOARD)
    #     input_name_new_dashboard.send_keys(name)
    #     logger.info('Name accepted')
    #
    # def click_button_add(self):
    #     logger.info('Click add button')
    #     click_button_add = self.driver.find_element(By.XPATH, LocatorsNewDashboard.LOCATOR_BUTTON_CONFIRM_ADD_NEW_DASHBOARD)
    #     click_button_add.click()
    #     logger.info('Add button is clicked')
    #
    # def click_button_delete_dashboard(self):
    #     logger.info('Click delete dashboard button')
    #     click_button_delete_dashboard = self.driver.find_element(By.XPATH,
    #                                                              LocatorsNewDashboard.LOCATOR_DELETE_DASHBOARD)
    #     click_button_delete_dashboard.click()
    #     logger.info('Delete dashboard button is clicked')
    #
    # def click_button_confirm_delete_dashboard(self):
    #     logger.info('Confirm delete dashboard')
    #     click_button_confirm_delete_dashboard = self.driver.find_element(By.XPATH,
    #                                                                      LocatorsNewDashboard.LOCATOR_CONFIRM_DELETE_DASHBOARD)
    #     click_button_confirm_delete_dashboard.click()
    #     logger.info('Confirmed dashboard deletion')
    #
    # def click_button_add_new_widget(self):
    #     logger.info('Click add new widget button')
    #     click_button_add_new_widget = self.driver.find_element(By.XPATH, LocatorsNewWidget.LOCATOR_ADD_NEW_WIDGET)
    #     click_button_add_new_widget.click()
    #     logger.info('Add new widget dashboard button is clicked')
    #
    # def click_dashboard_name(self):
    #     logger.info('Click dashboard name ')
    #     click_dashboard_name = self.driver.find_element(By.XPATH, LocatorsNewDashboard.LOCATOR_DASHBOARD_NAME)
    #     click_dashboard_name.click()
    #     logger.info('Dashboard name is clicked')
    #
    # def click_button_widget_launch_statistics_chart(self):
    #     logger.info('Click widget launch statistics chart button')
    #     click_button_widget_launch_statistics_chart = self.driver.find_element(By.XPATH,
    #                                                                            LocatorsNewWidget.LOCATOR_WIDGET_LAUNCH_STATISTICS_CHART)
    #     click_button_widget_launch_statistics_chart.click()
    #     logger.info('Widget launch statistics chart button is clicked')
    #
    # def click_button_widget_type_next_step(self):
    #     logger.info('Click next step button')
    #     click_button_widget_type_next_step = self.driver.find_element(By.XPATH,
    #                                                                   LocatorsNewWidget.LOCATOR_WIDGET_TYPE_NEXT_STEP)
    #     click_button_widget_type_next_step.click()
    #     logger.info('Next step button is clicked')
    #
    # def click_button_configure_widget_filter_sddf(self):
    #     logger.info('Click widget filter sddf button')
    #     click_button_configure_widget_filter_sddf = self.driver.find_element(By.XPATH,
    #                                                                          LocatorsNewWidget.LOCATOR_CONFIGURE_WIDGET_FILTER_SDDF)
    #     click_button_configure_widget_filter_sddf.click()
    #     logger.info('Widget filter sddf button is clicked')
    #
    # def click_button_configure_widget_type_next_step(self):
    #     logger.info('Click next step button')
    #     click_button_configure_widget_type_next_step = self.driver.find_element(By.XPATH,
    #                                                                             LocatorsNewWidget.LOCATOR_CONFIGURE_WIDGET_TYPE_NEXT_STEP)
    #     click_button_configure_widget_type_next_step.send_keys(Keys.ENTER)
    #     logger.info('Next step button is clicked')
    #
    # def click_button_save_add(self):
    #     logger.info('Click add button')
    #     click_button_save_add = self.driver.find_element(By.XPATH, LocatorsNewWidget.LOCATOR_SAVE_ADD)
    #     click_button_save_add.click()
    #     logger.info('Add button is clicked')

    # def click_button_editing_nickname(self):
    #     logger.info('Click editing nickname button')
    #     click_button_editing_nickname = self.driver.find_element(By.XPATH, LocatorsProfile.LOCATOR_EDITING_NICKNAM)
    #     click_button_editing_nickname.click()
    #     logger.info('Editing nickname button is clicked')
    #
    # def input_user_name(self, name):
    #     logger.info('Enter user name')
    #     input_user_name = self.driver.find_element(By.XPATH, LocatorsProfile.LOCATOR_USER_NAME)
    #     input_user_name.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
    #     input_user_name.send_keys(name)
    #     logger.info('User name accepted')
    #
    # def click_button_submit(self):
    #     logger.info('Click submit button')
    #     click_button_submit = self.driver.find_element(By.XPATH, LocatorsProfile.LOCATOR_SUBMIT)
    #     click_button_submit.click()
    #     logger.info('Submit button is clicked')
