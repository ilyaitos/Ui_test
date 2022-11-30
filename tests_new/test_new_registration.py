from test_new import TuningStart, TuningQuit, registration_page, config


class TestLogin(TuningStart, TuningQuit):

    def test_login(self):
        registration_page.input_login(config.get('Settings', 'login'))
        registration_page.input_password(config.get('Settings', 'password'))
        registration_page.click_button_login()
        registration_page.click_button_dashboard()
        assert registration_page.get_name_on_the_page_dashboard() == registration_page.get_name_dashboard()
