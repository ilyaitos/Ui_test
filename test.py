import random
import pytest
from selenium.webdriver.common.by import By
from locator import *
from conftest import driver, logger
from home_page import HomePage
from dashboard_page import DashboardPage, NameWidget
from profile_page import ProfilePage
from launches_page import LaunchesPage


home = HomePage(driver)
dashboard = DashboardPage(driver)
profile = ProfilePage(driver)
launches = LaunchesPage(driver)
url_dashboard_page = "http://localhost:8080/ui/#default_personal/"
url_registration_page = 'http://localhost:8080/ui/#login'
link = "http://localhost:8080/ui/#login"


@pytest.fixture(scope="module")
def login():
    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get(link)
    login = 'default'
    password = '1q2w3e'
    home.input_login(login)
    home.input_password(password)
    home.click_button_login()


@pytest.fixture(autouse=True, scope="module")
def add_new_dashboard(login):
    logger.info('Create new dashboard')
    name = 'Cat'
    home.click_button_dashboard()
    dashboard.click_button_add_new_dashboard()
    dashboard.input_name_new_dashboard(name)
    dashboard.click_button_add()
    logger.info('New dashboard created by')

#тип, фильтр
@pytest.fixture(autouse=True, scope="module")
def add_new_widget(login):
    logger.info('Create new widget')
    name = NameWidget.LAUNCH_STATISTICS_CHART
    home.click_button_dashboard()
    dashboard.click_dashboard_name()
    dashboard.click_button_add_new_widget()
    dashboard.click_button_widget_launch_statistics_chart(name)
    dashboard.click_button_widget_type_next_step()
    dashboard.click_button_configure_widget_filter_sddf()
    dashboard.click_button_configure_widget_type_next_step()
    dashboard.click_button_save_add()
    logger.info('New widget created by')

# обект дпш борд

@pytest.fixture(autouse=True, scope="module")
def delete_dashboard(login):
    yield
    logger.info('Delete dashboard')
    home.click_button_dashboard()
    list_name = dashboard.list_dashboard_name()
    count = len(list_name)
    while count > 0:
        home.click_button_dashboard()
        dashboard.click_button_delete_dashboard()
        dashboard.click_button_confirm_delete_dashboard()
        count -= 1
    logger.info('Dashboard deleted')

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

