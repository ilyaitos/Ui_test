from test_n import *


class TestDashboard(TuningTest):

    def test_project_settings(self):
        home.click_button_project_settings()
        assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "settings/general"
