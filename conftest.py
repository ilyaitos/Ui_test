import pytest
from selenium.webdriver.common.by import By
from locator import LocatorsRegistrationPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import os
from datetime import datetime


logger = logging.getLogger(__name__)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "http://localhost:8080/ui/#login"


@pytest.hookimpl
def pytest_runtest_setup(item):
    logging_plugin = item.config.pluginmanager.get_plugin("logging-plugin")
    timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d--%H-%M-%S')
    logging_plugin.set_log_path(os.path.join('logger_test', f'{item.name}_{timestamp}.log'))


@pytest.fixture(autouse=True, scope="module")
def login():
    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get(link)
    driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_LOGIN_FIELD).send_keys('default')
    driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_PASSWORD_FIELD).send_keys('1q2w3e')
    driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_BUTTON_TO_COME_IN).click()
    yield
    driver.quit()


@pytest.fixture(autouse=True)
def start_page():
    driver.get('http://localhost:8080/ui/#default_personal/dashboard')
