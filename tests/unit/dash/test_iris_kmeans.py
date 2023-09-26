from app.dash.iris_kmeans import (
    filter_options,
    init_callbacks,
    iris,
    make_graph,
)
import numpy as np
import plotly.graph_objs as go
import pytest


def test_filter_options():
    for col in iris.columns:
        assert {"label": col, "value": col, "disabled": True} in filter_options(col)


@pytest.fixture()
def mock_kmeans(mocker):
    mock = mocker.patch("app.dash.iris_kmeans.KMeans")
    mock.return_value.labels_ = np.array([0] * 150)
    mock.return_value.cluster_centers_ = np.array(
        [[5.77358491, 2.69245283], [6.81276596, 3.07446809], [5.006, 3.428]]
    )

    return mock


def test_make_graph(mock_kmeans):
    res = make_graph("sepal length (cm)", "sepal width (cm)", 3)

    assert isinstance(res, go.Figure)
    assert mock_kmeans.call_count == 1


def test_init_callbacks(mocker):
    mock_dash_app = mocker.Mock()

    assert init_callbacks(mock_dash_app) is mock_dash_app
    assert mock_dash_app.callback.call_count == 3
    assert mock_dash_app.callback.return_value.call_args_list == [
        mocker.call(make_graph),
        mocker.call(filter_options),
        mocker.call(filter_options),
    ]
