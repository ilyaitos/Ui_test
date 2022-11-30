from dashboard_page_new import Dashboard
from test_new import TuningRegistration, TuningQuit, dashboard_page


class TestDashboard(TuningRegistration, TuningQuit):

    @classmethod
    def teardown_class(cls):
        dashboard_page.delete_dashboard(['ilya'])
        super(TestDashboard, cls).teardown_class()

    def test_button_dashboard(self):
        dashboard_page.click_button_debug()
        dashboard_page.click_button_dashboard()
        assert dashboard_page.get_name_on_the_page_dashboard() == dashboard_page.get_name_dashboard()

    def test_add_new_dashboard(self):
        dashboard_name = 'ilya'
        dashboards = Dashboard(dashboard_name)
        dashboard_page.create_dashboard(dashboards)
        assert dashboard_page.get_dashboard_name(dashboard_name) == dashboard_name
