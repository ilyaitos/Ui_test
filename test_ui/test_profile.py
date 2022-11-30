from test import profile_page, config, login, start_page, exit_web
import random


def test_profile(login, start_page, exit_web):
    city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
    name = random.choice(city_list)
    profile_page.click_button_dashboard()
    profile_page.click_button_default_drop()
    profile_page.click_button_profile()
    profile_page.click_button_editing_nickname()
    profile_page.input_user_name(name)
    profile_page.click_button_submit()
    assert profile_page.user_name() == name


def test_profile_logout(login, start_page, exit_web):
    profile_page.click_button_dashboard()
    profile_page.click_button_default_drop()
    profile_page.click_button_logout()
    assert profile_page.current_url() == config.get('Settings', 'url_registration_page')
