import pytest
from selenium.webdriver.common.by import By
from locator import LocatorsRegistrationPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
#илья

# import logging
# import sys
# import pytest
# from reportportal_client import RPLogger

# @pytest.fixture(scope="session")
# def rp_logger():
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.DEBUG)
#     logging.setLoggerClass(RPLogger)
#     return logger


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('logger_test.log', mode='w')
formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(filename)s - %(funcName)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "http://localhost:8080/ui/#login"


@pytest.fixture(autouse=True, scope="module")
def login():
    logger.warning('THE TEST IS STARTED')
    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get(link)
    driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_LOGIN_FIELD).send_keys('default')
    driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_PASSWORD_FIELD).send_keys('1q2w3e')
    driver.find_element(By.XPATH, LocatorsRegistrationPage.LOCATOR_BUTTON_TO_COME_IN).click()
    yield
    driver.quit()
    logger.warning('TEST IS OVER')


@pytest.fixture(autouse=True)
def start_page():
    driver.get('http://localhost:8080/ui/#default_personal/dashboard')






