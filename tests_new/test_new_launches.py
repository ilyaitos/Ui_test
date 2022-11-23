from test_n import *


class TestDashboard(TuningTest):

    def test_launches(self):
        home.click_button_launches()
        assert home.current_url() == config.get('Settings', 'url_dashboard_page') + "launches/all"

    def test_dashboard_passed(self):
        home.click_button_dashboard()
        assert home.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"

    @pytest.mark.xfail(strict=True)
    def test_dashboard_failed(self):
        home.click_button_dashboard()
        assert home.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"

    @pytest.mark.skip
    def test_dashboard_skipped(self):
        home.click_button_dashboard()
        assert home.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"

    def test_status(self):
        home.click_button_launches()
        driver.refresh()
        launches.click_launches_example()
        pytest.assume('Passed' == launches.dashboard_status_passed())
        pytest.assume('Failed' == launches.dashboard_status_failed())
        pytest.assume('Skipped' == launches.dashboard_status_skipped())
