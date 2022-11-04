from test import *


def test_profile(login):
    city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
    name = random.choice(city_list)
    home.click_button_dashboard()
    driver.refresh()
    home.click_button_default_drop()
    home.click_button_profile()
    profile.click_button_editing_nickname()
    profile.input_user_name(name)
    profile.click_button_submit()
    driver.refresh()
    user_name = driver.find_element(By.XPATH, LocatorsProfile.LOCATOR_USER_NAME_ON_THE_PAGE)
    assert user_name.get_attribute("textContent") == name


def test_profile_logout(login):
    home.click_button_dashboard()
    driver.refresh()
    home.click_button_default_drop()
    home.click_button_logout()
    assert home.current_url() == url_registration_page
