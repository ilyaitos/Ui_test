import random
import pytest
from selenium.webdriver.common.by import By
from locator import *
from conftest import driver, logger
from home_page import HomePage
from dashboard_page import DashboardPage, NameWidget, ObjectsPage, NameFilter
from profile_page import ProfilePage
from launches_page import LaunchesPage


objects = ObjectsPage(driver)
home = HomePage(driver)
dashboard = DashboardPage(driver)
profile = ProfilePage(driver)
launches = LaunchesPage(driver)
url_dashboard_page = "http://localhost:8080/ui/#default_personal/"
url_registration_page = 'http://localhost:8080/ui/#login'
link = "http://localhost:8080/ui/#login"


dashboard_name_1 = 'ilya'
dashboard_name_2 = 'Cat'

list_dashboard_name = [dashboard_name_1, dashboard_name_2]


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
    objects.objects_dashboard(dashboard_name_1)
    logger.info('New dashboard created by')


@pytest.fixture(autouse=True, scope="module")
def add_new_widget(login):
    logger.info('Create new widget')
    type_widget = NameWidget.LAUNCH_STATISTICS_CHART
    name_filter = NameFilter.FILTER_1
    name_widget = 'GTA1'
    objects.objects_widget(dashboard_name_2, type_widget, name_filter, name_widget)
    logger.info('New widget created by')


@pytest.fixture(autouse=True, scope="module")
def delete_dashboard(login):
    yield
    objects.objects_delete_dashboard(list_dashboard_name)


def test_filters():
    home.click_button_filters()
    assert home.current_url() == url_dashboard_page + "filters"


def test_debug():
    home.click_button_debug()
    assert home.current_url() == url_dashboard_page + "userdebug/all"


def test_project_members():
    home.click_button_project_members()
    assert home.current_url() == url_dashboard_page + "members"


def test_project_settings():
    home.click_button_project_settings()
    assert home.current_url() == url_dashboard_page + "settings/general"

