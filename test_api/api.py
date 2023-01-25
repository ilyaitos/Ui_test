import requests
from pathlib import Path
import configparser
import pytest
import logging
import os
from datetime import datetime
from enum import Enum

path = Path(__file__)
os.chdir("C:/Users/User/PycharmProjects/pythonUI1/utils")
config_path = os.path.join("setting.ini")
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8-sig')

logger = logging.getLogger(__name__)


@pytest.hookimpl
def pytest_runtest_setup(item):
    logging_plugin = item.config.pluginmanager.get_plugin("logging-plugin")
    timestamp = datetime.strftime(datetime.now(), '[%Y-%m-%d]__%H-%M-%S')
    os.chdir("C:/Users/User/PycharmProjects/pythonUI1/")
    logging_plugin.set_log_path(os.path.join('logger', f'{item.name}__{timestamp}.log'))


POST_REGISTER_DASHBOARD = 'dashboard'
POST_REGISTER_WIDGET = 'widget'


class TypeWidgetApi(Enum):
    Launch_statistics_chart = 'statisticTrend'
    OVERALL_STSTISTICS = 'overallStatistics'


class NameFilterApi(Enum):
    filter_sorted_by_start_time = 245
    filter_sorted_by_launch_name = 244
    filter_filter_sorted_by_total = 246


class ApiDashboard:
    def __init__(self, name):
        self.name = name


class ApiWidget:
    def __init__(self, name, widgetType, filterIds):
        self.name = name
        self.widgetType = widgetType
        self.filterIds = filterIds
        self.share = "false"


class Api:
    def __init__(self):
        self.url = f"{config.get('Settings', 'uri_api')}"
        self.project_name = f"{config.get('Settings', 'projectName')}"
        self.access_token = config.get('Settings', 'access_token')

    def create_api_dashboard(self, ApiDashboard):
        body = {"description": '',
                "name": ApiDashboard.name,
                "share": 'False'}
        response_api = requests.post(f'{self.url}{self.project_name}{POST_REGISTER_DASHBOARD}', json=body,
                                     headers={'Authorization': self.access_token})
        logger.info(response_api.json())
        return response_api

    def create_api_widget(self, ApiWidget):
        body = {
            "contentParameters": {
                "contentFields": [
                    "statistics$executions$total",
                    "statistics$executions$passed",
                    "statistics$executions$failed",
                    "statistics$executions$skipped",
                    "statistics$defects$product_bug$pb001",
                    "statistics$defects$automation_bug$ab001",
                    "statistics$defects$system_issue$si001",
                    "statistics$defects$no_defect$nd001",
                    "statistics$defects$to_investigate$ti001"
                ],
                "itemsCount": 50,
                "widgetOptions": {
                    "zoom": "false",
                    "timeline": "launch",
                    "viewMode": "area-spline"
                }
            },
            "description": "",
            "filterIds": [ApiWidget.filterIds],
            "name": ApiWidget.name,
            "share": "false",
            "widgetType": ApiWidget.widgetType
        }
        response_api = requests.post(f'{self.url}{self.project_name}{POST_REGISTER_WIDGET}', json=body,
                                     headers={'Authorization': self.access_token})
        logger.info(response_api.json())
        return response_api

    def add_widget_to_specified_dashboard(self, id_dashboard, id_widget):
        body = {"addWidget": {
            "share": "true",
            "widgetId": id_widget,
            "widgetName": "",
            "widgetOptions": {
                "zoom": "false",
                "timeline": "launch",
                "viewMode": "area-spline"},
            "widgetPosition": {
                "positionX": 0,
                "positionY": 0
            },
            "widgetSize": {
                "height": 5,
                "width": 5
            },
            "widgetType": "statisticTrend"
        }
        }
        response_api = requests.put(f'{self.url}{self.project_name}{POST_REGISTER_DASHBOARD}/{id_dashboard}/add',
                                    json=body, headers={'Authorization': self.access_token})
        logger.info(response_api.json())
        return response_api

    def delete_api_dashboard(self, id_dashboard):
        requests.delete(f'{self.url}{self.project_name}{POST_REGISTER_DASHBOARD}/{id_dashboard}',
                        headers={'Authorization': self.access_token})

    def add_api_test_run(self):
        body = {"createDashboard": 'true'}
        response_api = requests.post(f'{self.url}demo/{self.project_name}', json=body,
                                     headers={'Authorization': self.access_token})
        logger.info(response_api.json())
        return response_api

    def get_widget_by_id(self, id_widget):
        response_api = requests.get(f'{self.url}{self.project_name}{POST_REGISTER_WIDGET}/{id_widget}', headers={'Authorization': self.access_token})
        logger.info(response_api.json())
        return response_api

    def get_dashboard_by_id(self, id_dashboard):
        response_api = requests.get(f'{self.url}{self.project_name}{POST_REGISTER_DASHBOARD}/{id_dashboard}', headers={'Authorization': self.access_token})
        logger.info(response_api.json())
        return response_api
#wwwwwww