from test import *


def test_dashboard(login):
    home.click_button_dashboard()
    assert home.current_url() == url_dashboard_page + "dashboard"


def test_add_new_dashboard(login):
    objects.objects_dashboard(dashboard_name_1)
    driver.refresh()
    assert dashboard.dashboard_name().count(dashboard_name_1) > 0


def test_add_new_widget(login):
    type_widget = NameWidget.LAUNCH_STATISTICS_CHART
    name_filter = NameFilter.FILTER_1
    name_widget = 'Dog1'
    objects.objects_widget(dashboard_name_2, type_widget, name_filter, name_widget)
    assert dashboard.widget_name() == name_widget
