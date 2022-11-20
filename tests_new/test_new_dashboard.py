from test import *
from dashboard_page import Dashboard, Widget
from waiter import wait
from test_n import *


def setup_module(module):
    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get(config.get('Settings', 'link'))
    registration.input_login(config.get('Settings', 'login'))
    registration.input_password(config.get('Settings', 'password'))
    registration.click_button_login()


def setup_method(test_method):
    driver.get('http://localhost:8080/ui/#default_personal/dashboard')


def test_dashboard():
    home.click_button_dashboard()
    assert home.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"


def test_add_new_dashboard():
    dashboard_name = 'ilya'
    dashboards = Dashboard(dashboard_name)
    dashboard.create_dashboard(dashboards)
    driver.refresh()
    assert dashboard.find_dashboard_name(dashboard_name) == dashboard_name


def test_add_new_widget():
    dashboard_name = 'ilya'
    type_widget = NameWidget.LAUNCH_STATISTICS_CHART.value
    name_filter = NameFilter.FILTER_1.value
    name_widget = 'Dog3'
    widget = Widget(dashboard_name, type_widget, name_filter, name_widget)
    dashboard.create_widget(widget)
    search_dashboard_name = dashboard.search_dashboard_name()
    wait(3)
    search_name_widget = dashboard.search_name_widget()
    dashboard.click()
    search_name_filter = dashboard.search_name_filter()
    search_type_widget = dashboard.search_type_widget()
    pytest.assume(dashboard_name == search_dashboard_name)
    pytest.assume('Launch statistics chart' == search_type_widget)
    #pytest.assume(name_widget == search_name_widget)
    pytest.assume('filter_1' == search_name_filter)

def teardown_module(module):
    dashboard.delete_dashboard(['ilya', 'Cat'])
    driver.quit()