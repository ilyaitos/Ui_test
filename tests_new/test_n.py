from test import *


class TuningTest:
    @classmethod
    def setup_class(cls):
        driver.implicitly_wait(7)
        driver.maximize_window()
        driver.get(config.get('Settings', 'link'))
        registration.input_login(config.get('Settings', 'login'))
        registration.input_password(config.get('Settings', 'password'))
        registration.click_button_login()

    @classmethod
    def teardown_class(cls):
        driver.quit()

    def setup_method(self):
        driver.get('http://localhost:8080/ui/#default_personal/dashboard')


class TuningTest1(TuningTest):
    @classmethod
    def setup_class(cls):
        super().setup_class()
        dashboard_name = 'Cat'
        dashboards = Dashboard(dashboard_name)
        dashboard.create_dashboard(dashboards)
