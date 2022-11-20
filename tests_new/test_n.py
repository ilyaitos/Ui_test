from conftest import *
from test import *


def add_new_dashboard():
    logger.info('Create new dashboard')
    dashboard_name = 'Cat'
    dashboards = Dashboard(dashboard_name)
    dashboard.create_dashboard(dashboards)
    logger.info('New dashboard created by')



def add_new_widget():
    logger.info('Create new widget')
    dashboard_name = 'Cat'
    type_widget = NameWidget.LAUNCH_STATISTICS_CHART.value
    name_filter = NameFilter.FILTER_1.value
    name_widget = 'Dog2'
    widget = Widget(dashboard_name, type_widget, name_filter, name_widget)
    dashboard.create_widget(widget)
    logger.info('New widget created by')



def delete_dashboard():
    yield
    dashboard.delete_dashboard(['ilya', 'Cat'])