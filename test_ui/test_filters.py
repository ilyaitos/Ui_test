from test import *


def test_filters(login, start_page):
    home.click_button_filters()
    assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "filters"