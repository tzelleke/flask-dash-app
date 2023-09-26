import importlib

import pytest


@pytest.mark.parametrize(
    ("module_name", "route_pathname_prefix"),
    [
        ("iris_kmeans", "/iris-k-means/"),
        ("crossfilter_example", "/crossfilter-example/"),
    ],
)
def test_init_dash(
    module_name,
    route_pathname_prefix,
    mock_dash_constructor,
    mock_dash_layout_property,
    mocker,
):
    m = importlib.import_module(f"app.dash.{module_name}")
    mock_init_callbacks = mocker.patch.object(m, "init_callbacks")
    server = mocker.sentinel.server

    res = m.init_dash(server)
    dash_app = mock_dash_constructor.mock_calls[0][1][0]

    assert res is server
    mock_dash_constructor.assert_called_once_with(
        dash_app, server, route_pathname_prefix
    )
    mock_dash_layout_property.assert_called_once_with(m.app_layout)
    mock_init_callbacks.assert_called_once_with(dash_app)
