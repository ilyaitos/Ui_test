from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from home_page_new import HomePage
from dashboard_page_new import DashboardPage
from profile_page_new import ProfilePage
from launches_page_new import LaunchesPage
from registration_page_new import RegistrationPage
import configparser
from pathlib import Path
import os

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


class TuningStart:
    @classmethod
    def setup_class(cls):
        driver.implicitly_wait(7)
        driver.maximize_window()
        driver.get(config.get('Settings', 'link'))


class TuningRegistration(TuningStart):

    @classmethod
    def setup_class(cls):
        super(TuningRegistration, cls).setup_class()
        registration_page.input_login(config.get('Settings', 'login'))
        registration_page.input_password(config.get('Settings', 'password'))
        registration_page.click_button_login()

    def setup_method(self):
        driver.get('http://localhost:8080/ui/#default_personal/dashboard')


class TuningQuit:
    @classmethod
    def teardown_class(cls):
        driver.quit()
