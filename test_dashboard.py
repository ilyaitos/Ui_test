from test import *


def test_dashboard(login):
    home.click_button_dashboard()
    assert home.current_url() == url_dashboard_page + "dashboard"


def test_add_new_dashboard(login):
    name = 'ilya'
    dashboard.click_button_add_new_dashboard()
    dashboard.input_name_new_dashboard(name)
    dashboard.click_button_add()
    driver.refresh()
    assert dashboard.dashboard_name().count(name) > 0


def test_add_new_widget(login):
    name = NameWidget.LAUNCH_STATISTICS_CHART
    dashboard.click_dashboard_name()
    dashboard.click_button_add_new_widget()
    dashboard.click_button_widget_launch_statistics_chart(name)
    dashboard.click_button_widget_type_next_step()
    dashboard.click_button_configure_widget_filter_sddf()
    dashboard.click_button_configure_widget_type_next_step()
    dashboard.click_button_save_add()
    assert dashboard.widget_name() != []
