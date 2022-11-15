from test import *


def test_debug():
    home.click_button_debug()
    assert home.current_url() == config.get('Settings', 'url_dashboard_page') + "userdebug/all"