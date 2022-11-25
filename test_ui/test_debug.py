from test import *


def test_debug(login, start_page):
    home.click_button_debug()
    assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "userdebug/all"