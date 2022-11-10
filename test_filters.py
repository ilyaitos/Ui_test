from test import *


def test_filters():
    home.click_button_filters()
    assert home.current_url() == url_dashboard_page + "filters"