from test import *


def test_login():
    driver.implicitly_wait(7)
    driver.get(config.get('Settings', 'link'))
    registration_page.input_login(config.get('Settings', 'login'))
    registration_page.input_password(config.get('Settings', 'password'))
    registration_page.click_button_login()
    registration_page.click_button_dashboard()
    assert registration_page.get_name_on_the_page_dashboard() == registration_page.name_on_the_page_dashboard()
