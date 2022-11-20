from test import *


def test_project_members():
    home.click_button_project_members()
    assert home.current_url() == config.get('Settings', 'url_dashboard_page') + "members"