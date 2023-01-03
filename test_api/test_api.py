import pytest
from api import ApiDashboard, ApiWidget, Api, NameFilterApi, TypeWidgetApi
import unittest


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = Api()

    def test_api_create_dashboard(self):
        name_dashboard = 'dog'
        dashboard = ApiDashboard(name_dashboard)
        response = self.api.create_api_dashboard(dashboard)
        get_id_dashboard = response.json()['id']
        pytest.assume(get_id_dashboard != 0)
        pytest.assume(response.status_code == 201)
        pytest.assume(self.api.get_dashboard_by_id(get_id_dashboard).json()['name'] == name_dashboard)
        self.api.delete_api_dashboard(get_id_dashboard)

    def test_api_create_widget(self):
        name_dashboard = 'ilya'
        name_widget = 'anna'
        type_widget = TypeWidgetApi.Launch_statistics_chart.value
        name_filter = NameFilterApi.filter_sorted_by_launch_name.value
        widget = ApiWidget(name_widget, type_widget, name_filter)
        dashboard = ApiDashboard(name_dashboard)
        get_id_dashboard = self.api.create_api_dashboard(dashboard).json()['id']
        get_id_widget = self.api.create_api_widget(widget).json()['id']
        get_status_code = self.api.add_widget_to_specified_dashboard(get_id_dashboard, get_id_widget)
        pytest.assume(get_id_widget != 0)
        pytest.assume(get_status_code.status_code == 200)
        pytest.assume(self.api.get_widget_by_id(get_id_widget).json()['name'] == name_widget)
        self.api.delete_api_dashboard(get_id_dashboard)

    def test_api_run(self):
        response = self.api.add_api_test_run()
        get_id_dashboard = response.json()['dashboardId']
        pytest.assume(response.status_code == 200)
        pytest.assume(get_id_dashboard != 0)
        self.api.delete_api_dashboard(get_id_dashboard)


