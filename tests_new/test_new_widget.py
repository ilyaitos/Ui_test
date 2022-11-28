from test_n import *


class TestDashboard(TuningTestRegistration, TuningTestDelete):

    @classmethod
    def setup_class(cls):
        super(TestDashboard, cls).setup_class()
        dashboard_name = 'Cat'
        dashboards = Dashboard(dashboard_name)
        dashboard_page.create_dashboard(dashboards)

    def test_add_new_widget(self):
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
        pytest.assume(TypeWidget.Launch_statistics_chart.name.replace('_', ' ') == received_type_widget)
        pytest.assume(name_widget == received_name_widget)
        pytest.assume(NameFilter.filter_sorted_by_start_time.name == received_name_filter)

