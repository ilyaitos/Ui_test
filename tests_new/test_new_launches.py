import pytest
from test_new import TuningRegistration, TuningQuit, launches_page


class TestLaunches(TuningRegistration, TuningQuit):

    def test_launches(self):
        launches_page.click_button_launches()
        assert launches_page.get_name_on_the_page_launches() == launches_page.name_on_the_page_launches()

    def test_dashboard_passed(self):
        launches_page.click_button_debug()
        launches_page.click_button_dashboard()
        assert launches_page.get_name_on_the_page_dashboard() == launches_page.name_page_dashboard()

    @pytest.mark.xfail(strict=True)
    def test_dashboard_failed(self):
        launches_page.click_button_debug()
        launches_page.click_button_dashboard()
        assert launches_page.get_name_on_the_page_dashboard() == launches_page.name_page_dashboard()

    @pytest.mark.skip
    def test_dashboard_skipped(self):
        launches_page.click_button_debug()
        launches_page.click_button_dashboard()
        assert launches_page.get_name_on_the_page_dashboard() == launches_page.name_page_dashboard()

    def test_status(self):
        launches_page.click_button_launches()
        launches_page.click_launches_example()
        pytest.assume('Passed' == launches_page.dashboard_status_passed())
        pytest.assume('Failed' == launches_page.dashboard_status_failed())
        pytest.assume('Skipped' == launches_page.dashboard_status_skipped())
