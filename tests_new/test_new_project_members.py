from test_n import *


class TestDashboard(TuningTest):

    def test_project_members(self):
        home.click_button_project_members()
        assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "members"