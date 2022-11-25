from test import *
import random


def test_profile(login, start_page):
    city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
    name = random.choice(city_list)
    home.click_button_dashboard()
    home.click_button_default_drop()
    home.click_button_profile()
    profile.click_button_editing_nickname()
    profile.input_user_name(name)
    profile.click_button_submit()
    assert profile.user_name() == name


def test_profile_logout(login, start_page):
    home.click_button_dashboard()
    home.click_button_default_drop()
    home.click_button_logout()
    assert registration.current_url() == config.get('Settings', 'url_registration_page')
