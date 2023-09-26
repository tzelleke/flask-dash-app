from app.dash.demo import (
    app_layout,
    init_dash,
)


def test_init_dash(mock_dash_constructor, mock_dash_layout_property, mocker):
    server = mocker.sentinel.server

    res = init_dash(server)
    dash_app = mock_dash_constructor.mock_calls[0][1][0]

    assert res is server
    mock_dash_constructor.assert_called_once_with(dash_app, server, "/demo/")
    mock_dash_layout_property.assert_called_once_with(app_layout)
