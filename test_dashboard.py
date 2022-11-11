from test import *
from dashboard_page import Dashboard, Widget
from enum import Enum
#
# def test_dashboard(login):
#     home.click_button_dashboard()
#     assert home.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"


def test_add_new_dashboard(login):
    dashboard_name = 'ilya'
    dashboards = Dashboard(dashboard_name)
    dashboard.create_dashboard(dashboards)
    driver.refresh()

    #assert create_dashboard.name_dashboard == dashboard.search_dashboard_with_name(create_dashboard.name_dashboard)


def test_add_new_widget(login):
    dashboard_name = 'ilya'
    type_widget = NameWidget.LAUNCH_STATISTICS_CHART.value
    name_filter = NameFilter.FILTER_1.value
    name_widget = 'Dog1'
    widget = Widget(dashboard_name, type_widget, name_filter, name_widget)
    dashboard.create_widget(widget)
    new_widget = dashboard.get_widget()
    #assert name_widget == new_widget
