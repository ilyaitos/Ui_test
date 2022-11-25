from test import *
from dashboard_page import Dashboard, Widget
from waiter import wait


def test_dashboard(login, start_page):
    home.click_button_dashboard()
    assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"


def test_add_new_dashboard(login, start_page):
    dashboard_name = 'ilya'
    dashboards = Dashboard(dashboard_name)
    dashboard.create_dashboard(dashboards)
    assert dashboard.get_dashboard_name(dashboard_name) == dashboard_name


def test_add_new_widget(login, add_new_dashboard, start_page, delete_dashboard):
    dashboard_name = 'Cat'
    type_widget = TypeWidget.LAUNCH_STATISTICS_CHART.value
    name_filter = NameFilter.FILTER_SORTED_BY_START_TIME.value
    name_widget = 'Dog4'
    widget = Widget(dashboard_name, type_widget, name_filter, name_widget)
    dashboard.create_widget(widget)
    received_name_widget = dashboard.get_name_widget()
    dashboard.click_button_filter_properties()
    received_name_filter = dashboard.get_name_filter()
    received_type_widget = dashboard.get_type_widget()
    pytest.assume('Launch statistics chart' == received_type_widget)
    #pytest.assume(name_widget == received_name_widget)
    pytest.assume('filter_sorted_by_start_time' == received_name_filter)

