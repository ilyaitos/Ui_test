from test_n import *


def test_login():
    driver.implicitly_wait(7)
    driver.get(config.get('Settings', 'link'))
    registration.input_login(config.get('Settings', 'login'))
    registration.input_password(config.get('Settings', 'password'))
    registration.click_button_login()
    home.click_button_dashboard()
    assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"
