import pytest
from conftest import driver, logger
from home_page import HomePage
from dashboard_page import DashboardPage, NameWidget, NameFilter, Dashboard, Widget
from profile_page import ProfilePage
from launches_page import LaunchesPage
from registration_page import RegistrationPage
import configparser
from pathlib import Path
import os

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "C:/Users/User/PycharmProjects/pythonUI1/utils/setting.ini")
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8-sig')

registration = RegistrationPage(driver)
home = HomePage(driver)
dashboard = DashboardPage(driver)
profile = ProfilePage(driver)
launches = LaunchesPage(driver)


@pytest.fixture(scope="module")
def login():
    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get(config.get('Settings', 'link'))
    registration.input_login(config.get('Settings', 'login'))
    registration.input_password(config.get('Settings', 'password'))
    registration.click_button_login()


@pytest.fixture(scope="module")
def add_new_dashboard(login):
    logger.info('Create new dashboard')
    dashboard_name = 'Cat'
    dashboards = Dashboard(dashboard_name)
    dashboard.create_dashboard(dashboards)
    logger.info('New dashboard created by')


@pytest.fixture(scope="module")
def add_new_widget(login):
    logger.info('Create new widget')
    dashboard_name = 'Cat'
    type_widget = NameWidget.LAUNCH_STATISTICS_CHART.value
    name_filter = NameFilter.FILTER_1.value
    name_widget = 'Dog2'
    widget = Widget(dashboard_name, type_widget, name_filter, name_widget)
    dashboard.create_widget(widget)
    logger.info('New widget created by')


@pytest.fixture(scope="module")
def delete_dashboard(login):
    yield
    dashboard.delete_dashboard(['ilya'])
