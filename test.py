import random
import pytest
from selenium.webdriver.common.by import By
from locator import *
from conftest import driver
from home_page import HomePage
from dashboard_page import DashboardPage
from profile_page import ProfilePage
from waiter import wait


home = HomePage(driver)
dashboard = DashboardPage(driver)
profile = ProfilePage(driver)
url_dashboard_page = "http://localhost:8080/ui/#default_personal/"
url_registration_page = 'http://localhost:8080/ui/#login'


def test_dashboard():
    home.click_button_dashboard()
    assert home.current_url() == url_dashboard_page + "dashboard"

# def test_launches():
#     home.click_button_launches()
#     assert home.current_url() == url_dashboard_page + "launches/all"
#
#
# def test_filters():
#     home.click_button_filters()
#     assert home.current_url() == url_dashboard_page + "filters"
#
#
# def test_debug():
#     home.click_button_debug()
#     assert home.current_url() == url_dashboard_page + "userdebug/all"
#
#
# def test_project_members():
#     home.click_button_project_members()
#     assert home.current_url() == url_dashboard_page + "members"
#
#
# def test_project_settings():
#     home.click_button_project_settings()
#     assert home.current_url() == url_dashboard_page + "settings/general"
#
#
# def test_add_new_dashboard():
#     name = 'ilya'
#     home.click_button_dashboard()
#     dashboard.click_button_add_new_dashboard()
#     dashboard.input_name_new_dashboard(name)
#     dashboard.click_button_add()
#     home.click_button_dashboard()
#     dashboard.click_button_delete_dashboard()
#     dashboard.click_button_confirm_delete_dashboard()
#     home.click_button_dashboard()
#     assert dashboard.dashboard_name() == []

#
# def test_add_new_widget():
#     # popap
#     name = 'ilya'
#     home.click_button_dashboard()
#     dashboard.click_button_add_new_dashboard()
#     dashboard.input_name_new_dashboard(name)
#     dashboard.click_button_add()
#     home.click_button_dashboard()
#     dashboard.click_dashboard_name()
#     dashboard.click_button_add_new_widget()
#     dashboard.click_button_widget_launch_statistics_chart()
#     dashboard.click_button_widget_type_next_step()
#     dashboard.click_button_configure_widget_filter_sddf()
#     dashboard.click_button_configure_widget_type_next_step()
#     dashboard.click_button_save_add()
#     assert dashboard.widget_name() != []
#     home.click_button_dashboard()
#     dashboard.click_button_delete_dashboard()
#     dashboard.click_button_confirm_delete_dashboard()

#
# def test_profile():
#     city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
#     name = random.choice(city_list)
#     dashboard.click_button_dashboard()
#     home.click_button_default_drop()
#     home.click_button_profile()
#     profile.click_button_editing_nickname()
#     profile.input_user_name(name)
#     profile.click_button_submit()
#     driver.refresh()
#     user_name = driver.find_element(By.XPATH, LocatorsProfile.LOCATOR_USER_NAME_ON_THE_PAGE)
#     assert user_name.get_attribute("textContent") == name
#
# def test_profile_logout():
#     dashboard.click_button_dashboard()
#     home.click_button_default_drop()
#     home.click_button_logout()
#     assert home.current_url() == url_registration_page
#
#
# def test_login():
#     login = 'default'
#     password = '1q2w3e'
#     home.input_login(login)
#     home.input_password(password)
#     home.click_button_login()
#     home.click_button_dashboard()
#     assert home.current_url() == url_dashboard_page + "dashboard"
