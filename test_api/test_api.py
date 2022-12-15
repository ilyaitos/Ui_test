from api import response


class TestAPI:

    def test_api_create_dashboard(self):
        status_code = response.createDashboard_for_specified_project('', 'dog', 'False')
        assert status_code.status_code == 201

    def test_api_create_widet(self):
        get_id_dashboard = response.createDashboard_for_specified_project('', 'ilya', 'False').json()['id']
        get_id_widget = response.createNew_widget('anna').json()['id']
        get_status_code = response.add_widget_to_specified_dashboard(get_id_dashboard, get_id_widget)
        assert get_status_code.status_code == 200
