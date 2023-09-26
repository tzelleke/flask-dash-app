from app.dash.crossfilter_example import (
    init_callbacks,
    update_graph,
    update_x_timeseries,
    update_y_timeseries,
)


def test_init_callbacks(mocker):
    mock_dash_app = mocker.Mock()

    assert init_callbacks(mock_dash_app) is mock_dash_app
    assert mock_dash_app.callback.call_count == 3
    assert mock_dash_app.callback.return_value.call_args_list == [
        mocker.call(update_graph),
        mocker.call(update_y_timeseries),
        mocker.call(update_x_timeseries),
    ]
