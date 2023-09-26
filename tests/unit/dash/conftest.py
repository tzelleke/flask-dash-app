from app.dash.dash import Dash
import pytest


@pytest.fixture()
def mock_dash_constructor(mocker):
    mock = mocker.Mock()

    def mock_constructor(self, server, routes_pathname_prefix):
        print(self, server, routes_pathname_prefix)
        self.server = server
        self.routes_pathname_prefix = routes_pathname_prefix
        mock(self, server, routes_pathname_prefix)

    mocker.patch.object(Dash, "__init__", mock_constructor)

    return mock


@pytest.fixture()
def mock_dash_layout_property(mocker):
    return mocker.patch("app.dash.dash.Dash.layout", new_callable=mocker.PropertyMock)
