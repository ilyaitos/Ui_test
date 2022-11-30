import pytest
import logging
import os
from datetime import datetime


logger = logging.getLogger(__name__)


@pytest.hookimpl
def pytest_runtest_setup(item):
    logging_plugin = item.config.pluginmanager.get_plugin("logging-plugin")
    timestamp = datetime.strftime(datetime.now(), '[%Y-%m-%d]__%H-%M-%S')
    logging_plugin.set_log_path(os.path.join('C:/Users/User/PycharmProjects/pythonUI1/logger', f'{item.name}__{timestamp}.log'))
