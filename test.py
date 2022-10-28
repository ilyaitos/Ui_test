import random
from selenium.webdriver.common.by import By
from locator import *
from conftest import driver
from elements_page import ElementsPage
from time import sleep


elements = ElementsPage(driver)
url = "http://localhost:8080/ui/#default_personal/"


def test_1_login():
    driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_LOGIN_FIELD).send_keys('default')
    driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_PASSWORD_FIELD).send_keys('1q2w3e')
    elements.click_button_login()
    sleep(1)
    assert driver.current_url == url + "dashboard"


def test_2_dashboard():
    elements.click_button_dashboard()
    assert driver.current_url == url + "dashboard"


def test_3_launches():
    elements.click_button_launches()
    assert driver.current_url == url + "launches/all"


def test_4_filters():
    elements.click_button_filters()
    assert driver.current_url == url + "filters"


def test_5_debug():
    elements.click_button_debug()
    assert driver.current_url == url + "userdebug/all"


def test_6_project_members():
    elements.click_button_project_members()
    assert driver.current_url == url + "members"


def test_7_project_settings():
    elements.click_button_project_settings()
    assert driver.current_url == url + "settings/general"


def test_8_add_new_dashboard():
    name = 'ilya'
    elements.click_button_dashboard()
    elements.click_button_add_new_dashboard()
    elements.input_name_new_dashboard(name)
    elements.click_button_add()
    elements.click_button_dashboard()
    elements.click_button_delete_dashboard()
    elements.click_button_confirm_delete_dashboard()
    elements.click_button_dashboard()
    assert driver.find_elements(By.XPATH, LocatorsNewDashboard.LOCATOR_DASHBOARD_NAME) == []


def test_9_add_new_widget():
    name = 'ilya'
    elements.click_button_dashboard()
    elements.click_button_add_new_dashboard()
    elements.input_name_new_dashboard(name)
    elements.click_button_add()
    elements.click_button_dashboard()
    elements.click_dashboard_name()
    elements.click_button_add_new_widget()
    elements.click_button_widget_launch_statistics_chart()
    elements.click_button_widget_type_next_step()
    elements.click_button_configure_widget_filter_sddf()
    elements.click_button_configure_widget_type_next_step()
    elements.click_button_save_add()
    assert driver.find_elements(By.XPATH, LocatorsNewWidget.LOCATOR_WIDGET_NAME) != []
    elements.click_button_dashboard()
    elements.click_button_delete_dashboard()
    elements.click_button_confirm_delete_dashboard()


def test_10_profile():
    city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
    name = random.choice(city_list)
    driver.refresh()
    sleep(1)
    elements.click_button_default_drop()
    elements.click_button_profile()
    elements.click_button_editing_nickname()
    elements.input_user_name(name)
    elements.click_button_submit()
    driver.refresh()
    user_name = driver.find_element(By.XPATH, LocatorsProfile.LOCATOR_USER_NAME_ON_THE_PAGE)
    assert user_name.get_attribute("textContent") == name


def test_11_profile_logout():
    driver.refresh()
    sleep(1)
    elements.click_button_default_drop()
    elements.click_button_logout()
    assert driver.current_url == 'http://localhost:8080/ui/#login'
