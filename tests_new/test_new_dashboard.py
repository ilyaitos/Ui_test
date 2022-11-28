from test_n import *


class TestDashboard(TuningTestRegistration, TuningTestDelete):

    def test_button_dashboard(self):
        dashboard_page.click_button_debug()
        dashboard_page.click_button_dashboard()
        assert dashboard_page.get_name_on_the_page_dashboard() == dashboard_page.name_on_the_page_dashboard()

    def test_add_new_dashboard(self):
        dashboard_name = 'ilya'
        dashboards = Dashboard(dashboard_name)
        dashboard_page.create_dashboard(dashboards)
        assert dashboard_page.get_dashboard_name(dashboard_name) == dashboard_name
