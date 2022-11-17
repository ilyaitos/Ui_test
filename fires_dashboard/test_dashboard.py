from test import *
from dashboard_page import Dashboard, Widget


def test_dashboard(login):
    home.click_button_dashboard()
    assert home.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"


def test_add_new_dashboard(login):
    dashboard_name = 'ilya'
    dashboards = Dashboard(dashboard_name)
    dashboard.create_dashboard(dashboards)
    driver.refresh()
    assert dashboard.find_dashboard_name(dashboard_name) == dashboard_name


def test_add_new_widget(login):
    dashboard_name = 'ilya'
    type_widget = NameWidget.LAUNCH_STATISTICS_CHART.value
    name_filter = NameFilter.FILTER_1.value
    name_widget = 'Dog1'
    widget = Widget(dashboard_name, type_widget, name_filter, name_widget)
    dashboard.create_widget(widget)
    search_dashboard_name = dashboard.search_dashboard_name()
    search_name_widget = dashboard.search_name_widget()
    dashboard.click()
    search_name_filter = dashboard.search_name_filter()
    search_type_widget = dashboard.search_type_widget()
    pytest.assume(dashboard_name == search_dashboard_name)
    pytest.assume('Launch statistics chart' == search_type_widget)
    pytest.assume(name_widget == search_name_widget)
    pytest.assume('filter_1' == search_name_filter)

