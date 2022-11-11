from test import *
from dashboard_page import Dashboard, Widget


def test_dashboard(login):
    home.click_button_dashboard()
    assert home.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"


# def test_add_new_dashboard(login):
#     objects.objects_dashboard(dashboard_name_1)
#     driver.refresh()
#     assert dashboard.dashboard_name().count(dashboard_name_1) > 0
#
#
# def test_add_new_widget(login):
#     type_widget = NameWidget.LAUNCH_STATISTICS_CHART
#     name_filter = NameFilter.FILTER_1
#     name_widget = 'Dog1'
#     objects.objects_widget(dashboard_name_2, type_widget, name_filter, name_widget)
#     assert dashboard.widget_name() == name_widget

#
# def test_add_new_dashboard(login):
#
#     create_dashboard = Dashboard('ilya')
#     home.click_button_dashboard()
#     dashboard.click_button_add_new_dashboard()
#     dashboard.input_name_dashboard(create_dashboard.name_dashboard)
#     dashboard.click_button_add()
#     driver.refresh()
#     assert create_dashboard.name_dashboard == dashboard.search_dashboard_with_name(create_dashboard.name_dashboard)
#
# #коифигул
#     # assert dashboard.dashboard_name().count(dashboard_name_1) > 0
#
# def test_add_new_widget(login):
#     dashboard_name = 'ilya'
#     type_widget = NameWidget.LAUNCH_STATISTICS_CHART
#     name_filter = NameFilter.FILTER_1
#     name_widget = 'Dog1'
#     widget = Widget(dashboard_name, type_widget, name_filter, name_widget)
#     dashboard.create_widget(widget)
#     new_widget = dashboard.get_widget()
#     assert name_widget == new_widget
