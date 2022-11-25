from test_n import *


class TestDashboard(TuningTest):

    def test_filters(self):
        home.click_button_filters()
        assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "filters"