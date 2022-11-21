from test import *


def setup_module(module):
    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get(config.get('Settings', 'link'))
    registration.input_login(config.get('Settings', 'login'))
    registration.input_password(config.get('Settings', 'password'))
    registration.click_button_login()


def setup_method(test_method):
    driver.get('http://localhost:8080/ui/#default_personal/dashboard')


def add_new_dashboard():
    logger.info('Create new dashboard')
    dashboard_name = 'Cat'
    dashboards = Dashboard(dashboard_name)
    dashboard.create_dashboard(dashboards)
    logger.info('New dashboard created by')


def add_new_widget():
    logger.info('Create new widget')
    dashboard_name = 'Cat'
    type_widget = NameWidget.LAUNCH_STATISTICS_CHART.value
    name_filter = NameFilter.FILTER_1.value
    name_widget = 'Dog2'
    widget = Widget(dashboard_name, type_widget, name_filter, name_widget)
    dashboard.create_widget(widget)
    logger.info('New widget created by')


def teardown_module(module):
    dashboard.delete_dashboard(['ilya'])
    driver.quit()