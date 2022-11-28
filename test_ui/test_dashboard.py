from test import *
from dashboard_page import Dashboard, Widget


def test_dashboard(login):
    dashboard_page.click_button_debug()
    dashboard_page.click_button_dashboard()
    assert dashboard_page.get_name_on_the_page_dashboard() == dashboard_page.name_on_the_page_dashboard()


def test_add_new_dashboard(login, start_page):
    dashboard_name = 'ilya'
    dashboards = Dashboard(dashboard_name)
    dashboard_page.create_dashboard(dashboards)
    assert dashboard_page.get_dashboard_name(dashboard_name) == dashboard_name


def test_add_new_widget(login, add_new_dashboard, start_page, delete_dashboard):
    dashboard_name = 'Cat'
    type_widget = TypeWidget.Launch_statistics_chart.value
    name_filter = NameFilter.filter_sorted_by_start_time.value
    name_widget = 'Dog4'
    widget = Widget(dashboard_name, type_widget, name_filter, name_widget)
    dashboard_page.create_widget(widget)
    received_name_widget = dashboard_page.get_name_widget()
    dashboard_page.click_button_filter_properties()
    received_name_filter = dashboard_page.get_name_filter()
    received_type_widget = dashboard_page.get_type_widget()
    pytest.assume('Launch statistics chart' == received_type_widget)
    #pytest.assume(name_widget == received_name_widget)
    pytest.assume('filter_sorted_by_start_time' == received_name_filter)

