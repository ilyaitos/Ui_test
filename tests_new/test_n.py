from test import *


class TestClass:
    @classmethod
    def setup_class(cls):
        driver.implicitly_wait(7)
        driver.maximize_window()
        driver.get(config.get('Settings', 'link'))
        registration.input_login(config.get('Settings', 'login'))
        registration.input_password(config.get('Settings', 'password'))
        registration.click_button_login()

    @classmethod
    def setup_method(cls):
        driver.get('http://localhost:8080/ui/#default_personal/dashboard')

    @classmethod
    def add_new_dashboard(cls):
        logger.info('Create new dashboard')
        dashboard_name = 'Cat'
        dashboards = Dashboard(dashboard_name)
        dashboard.create_dashboard(dashboards)
        logger.info('New dashboard created by')

    @classmethod
    def add_new_widget(cls):
        logger.info('Create new widget')
        dashboard_name = 'Cat'
        type_widget = NameWidget.LAUNCH_STATISTICS_CHART.value
        name_filter = NameFilter.FILTER_1.value
        name_widget = 'Dog2'
        widget = Widget(dashboard_name, type_widget, name_filter, name_widget)
        dashboard.create_widget(widget)
        logger.info('New widget created by')





def teardown_module(module):
    driver.quit()