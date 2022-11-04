from test import *

#
# def test_dashboard(login):
#     home.click_button_dashboard()
#     assert home.current_url() == url_dashboard_page + "dashboard"

#
# def test_add_new_dashboard(login):
#     name = 'ilya'
#     objects.objects_dashboard(name)
#     driver.refresh()
#     assert dashboard.dashboard_name().count(name) > 0


def test_add_new_widget(login):
    name_widget = NameWidget.LAUNCH_STATISTICS_CHART
    name_filter = LocatorsNameFilter.LOCATOR_FILTER_1

    dashboard.click_dashboard_name()
    dashboard.click_button_add_new_widget()
    dashboard.click_button_widget_launch_statistics_chart(name_widget)
    dashboard.click_button_widget_type_next_step()
    dashboard.click_button_configure_widget_filter(name_filter)
    dashboard.click_button_configure_widget_type_next_step()
    dashboard.input_widget_name(name_widget='Dog2')
    dashboard.click_button_save_add()
    assert dashboard.widget_name() != []
