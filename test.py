import pytest
from conftest import driver, logger
from home_page import HomePage
from dashboard_page import DashboardPage, NameWidget, ObjectsPage, NameFilter
from profile_page import ProfilePage
from launches_page import LaunchesPage
from registration_page import RegistrationPage
import configparser


config = configparser.ConfigParser()
config.read('settings.ini', encoding='utf-8-sig')
registration = RegistrationPage(driver)
objects = ObjectsPage(driver)
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

#
# @pytest.fixture(autouse=True, scope="module")
# def add_new_dashboard(login):
#     logger.info('Create new dashboard')
#     objects.objects_dashboard(dashboard_name_1)
#     logger.info('New dashboard created by')
#
#
# @pytest.fixture(autouse=True, scope="module")
# def add_new_widget(login):
#     logger.info('Create new widget')
#     type_widget = NameWidget.LAUNCH_STATISTICS_CHART
#     name_filter = NameFilter.FILTER_1
#     name_widget = 'GTA1'
#     objects.objects_widget(dashboard_name_2, type_widget, name_filter, name_widget)
#     logger.info('New widget created by')
#

@pytest.fixture(autouse=True, scope="module")
def delete_dashboard(login):
    yield
    dashboard.delete_dashboard(['ilya', 'Cat'])
