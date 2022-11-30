import pytest
from test import launches_page, dashboard_page, login, start_page, add_new_dashboard, delete_dashboard, exit_web


def test_launches(login, start_page):
    launches_page.click_button_launches()
    assert launches_page.get_name_on_the_page_launches() == launches_page.name_on_the_page_launches()


def test_dashboard_passed(login, start_page):
    dashboard_page.click_button_debug()
    dashboard_page.click_button_dashboard()
    assert dashboard_page.get_name_on_the_page_dashboard() == dashboard_page.name_page_dashboard()


@pytest.mark.xfail(strict=True)
def test_dashboard_failed(login, start_page):
    dashboard_page.click_button_debug()
    dashboard_page.click_button_dashboard()
    assert dashboard_page.get_name_on_the_page_dashboard() == dashboard_page.name_page_dashboard()


@pytest.mark.skip
def test_dashboard_skipped(login, start_page):
    dashboard_page.click_button_debug()
    dashboard_page.click_button_dashboard()
    assert dashboard_page.get_name_on_the_page_dashboard() == dashboard_page.name_page_dashboard()


def test_status(login, start_page):
    launches_page.click_button_launches()
    launches_page.click_launches_example()
    pytest.assume('Passed' == launches_page.dashboard_status_passed())
    pytest.assume('Failed' == launches_page.dashboard_status_failed())
    pytest.assume('Skipped' == launches_page.dashboard_status_skipped())
