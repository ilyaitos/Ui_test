from test import *


def test_login():
    driver.implicitly_wait(7)
    driver.get(link)
    login = 'default'
    password = '1q2w3e'
    registration.input_login(login)
    registration.input_password(password)
    registration.click_button_login()
    home.click_button_dashboard()
    assert home.current_url() == url_dashboard_page + "dashboard"
