import requests
from pathlib import Path
import configparser
import pytest
import logging
import os
from datetime import datetime

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "C:/Users/User/PycharmProjects/pythonUI1/utils/setting.ini")
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8-sig')

logger = logging.getLogger(__name__)


@pytest.hookimpl
def pytest_runtest_setup(item):
    logging_plugin = item.config.pluginmanager.get_plugin("logging-plugin")
    timestamp = datetime.strftime(datetime.now(), '[%Y-%m-%d]__%H-%M-%S')
    logging_plugin.set_log_path(os.path.join('C:/Users/User/PycharmProjects/pythonUI1/logger', f'{item.name}__{timestamp}.log'))


url = f"{config.get('Settings', 'uri_api')}{config.get('Settings', 'projectName')}"


class Register:

    def __init__(self, url):
        self.url = url

    POST_REGISTER_DASHBOARD = 'dashboard'
    POST_REGISTER_WIDGET = 'widget'

    def createDashboard_for_specified_project(self, description, name, share):

        body = {"description": description,
                "name": name,
                "share": share}
        status_code_api = requests.post(f'{self.url}{self.POST_REGISTER_DASHBOARD}', json=body, headers={'Authorization': config.get('Settings', 'access_token')})
        logger.info(status_code_api.json())
        logger.info('List dashboard name found')
        return status_code_api

    def createNew_widget(self, name):
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
            "filterIds": [244],
            "name": name,
            "share": "false",
            "widgetType": "statisticTrend"
        }
        status_code_api = requests.post(f'{self.url}{self.POST_REGISTER_WIDGET}', json=body, headers={'Authorization': config.get('Settings', 'access_token')})
        logger.info(status_code_api.json())
        return status_code_api

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
        status_code_api = requests.put(f'{self.url}{self.POST_REGISTER_DASHBOARD}/{id_dashboard}/add', json=body, headers={'Authorization': config.get('Settings', 'access_token')})
        logger.info(status_code_api.json())
        return status_code_api


response = Register(url)
