from test import *


def setup_module(module):
    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get(config.get('Settings', 'link'))


def teardown_module(module):
    driver.quit()


class TuningRegistration:
    @classmethod
    def setup_class(cls):
        registration_page.input_login(config.get('Settings', 'login'))
        registration_page.input_password(config.get('Settings', 'password'))
        registration_page.click_button_login()

    def setup_method(self):
        driver.get('http://localhost:8080/ui/#default_personal/dashboard')


class TuningDelete:
    @classmethod
    def teardown_class(cls):
        dashboard_page.delete_dashboard(['ilya', 'Cat'])

