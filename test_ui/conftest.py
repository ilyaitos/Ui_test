import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import os
from datetime import datetime


logger = logging.getLogger(__name__)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


@pytest.hookimpl
def pytest_runtest_setup(item):
    logging_plugin = item.config.pluginmanager.get_plugin("logging-plugin")
    timestamp = datetime.strftime(datetime.now(), '[%Y-%m-%d]__%H-%M-%S')
    logging_plugin.set_log_path(os.path.join('logger', f'{item.name}__{timestamp}.log'))


@pytest.fixture(autouse=True, scope="module")
def exit_web():
    yield
    driver.quit()


@pytest.fixture(autouse=True)
def start_page():
    driver.get('http://localhost:8080/ui/#default_personal/dashboard')
