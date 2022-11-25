from test import *


def test_launches(login, start_page):
    home.click_button_launches()
    assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "launches/all"


def test_dashboard_passed(login, start_page):
    home.click_button_dashboard()
    assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"


@pytest.mark.xfail(strict=True)
def test_dashboard_failed(login, start_page):
    home.click_button_dashboard()
    assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"


@pytest.mark.skip
def test_dashboard_skipped(login, start_page):
    home.click_button_dashboard()
    assert registration.current_url() == config.get('Settings', 'url_dashboard_page') + "dashboard"


def test_status(login, start_page):
    home.click_button_launches()
    launches.click_launches_example()
    pytest.assume('Passed' == launches.dashboard_status_passed())
    pytest.assume('Failed' == launches.dashboard_status_failed())
    pytest.assume('Skipped' == launches.dashboard_status_skipped())
