import pytest
from home_page import HomePage
from dashboard_page import DashboardPage, Dashboard, Widget, TypeWidget, NameFilter
from profile_page import ProfilePage
from launches_page import LaunchesPage
from registration_page import RegistrationPage
import configparser
from pathlib import Path
import os
from log import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "C:/Users/User/PycharmProjects/pythonUI1/utils/setting.ini")
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8-sig')

registration_page = RegistrationPage(driver)
home_page = HomePage(driver)
dashboard_page = DashboardPage(driver)
profile_page = ProfilePage(driver)
launches_page = LaunchesPage(driver)


@pytest.fixture(scope="module")
def login():
    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get(config.get('Settings', 'link'))
    registration_page.input_login(config.get('Settings', 'login'))
    registration_page.input_password(config.get('Settings', 'password'))
    registration_page.click_button_login()


@pytest.fixture(scope="module")
def add_new_dashboard(login):
    logger.info('Create new dashboard')
    dashboard_name = 'Cat'
    dashboards = Dashboard(dashboard_name)
    dashboard_page.create_dashboard(dashboards)
    logger.info('New dashboard created by')


@pytest.fixture(scope="module")
def delete_dashboard(login):
    yield
    dashboard_page.delete_dashboard(['ilya', 'Cat'])
###############################################################################

@pytest.fixture(scope="module")
def exit_web():
    yield
    driver.quit()


@pytest.fixture()
def start_page():
    driver.get('http://localhost:8080/ui/#default_personal/dashboard')