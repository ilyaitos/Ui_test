from test_n import *


class TestDashboard(TuningTest):

    def test_debug(self):
        home.click_button_debug()
        assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "userdebug/all"