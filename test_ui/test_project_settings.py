from test import *


def test_project_settings(login, start_page):
    home.click_button_project_settings()
    assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "settings/general"

