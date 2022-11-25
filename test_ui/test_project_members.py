from test import *


def test_project_members(login, start_page):
    home.click_button_project_members()
    assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "members"