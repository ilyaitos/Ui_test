from test_n import *


class TestDashboard(TuningTest1):

    @classmethod
    def setup_class(cls):
        super().setup_class()

    def test_dashboard(self):
        home.click_button_dashboard()
        assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"

    def test_add_new_dashboard(self):
        dashboard_name = 'ilya'
        dashboards = Dashboard(dashboard_name)
        dashboard.create_dashboard(dashboards)
        assert dashboard.get_dashboard_name(dashboard_name) == dashboard_name

    def test_add_new_widget(self):
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
        pytest.assume(name_widget == received_name_widget)
        pytest.assume('filter_sorted_by_start_time' == received_name_filter)

    @classmethod
    def teardown_class(cls):
        dashboard.delete_dashboard(['ilya', 'Cat'])
        super().teardown_class()


