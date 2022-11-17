from test import *


def test_project_settings():
    home.click_button_project_settings()
    assert home.current_url() == config.get('Settings', 'url_dashboard_page') + "settings/general"

