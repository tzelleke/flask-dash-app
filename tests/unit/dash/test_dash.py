from app.dash.dash import Dash
from dash import Dash as BaseDash
from markupsafe import Markup
import pytest


@pytest.fixture()
def _mock_render_template(monkeypatch) -> None:
    def patch_render_template(*args, **kwargs):
        return args, kwargs

    monkeypatch.setattr("app.dash.dash.render_template", patch_render_template)


@pytest.mark.usefixtures("_mock_render_template")
def test_interpolate_index():
    assert issubclass(Dash, BaseDash)

    dash = Dash(__name__)

    res = dash.interpolate_index(
        metas="METAS",
        title="silently discarded",
        css="CSS",
        config="DASH_CONFIG",
        scripts="SCRIPTS",
        app_entry="APP_ENTRY",
        favicon="silently discarded",
        renderer="RENDERER",
    )

    assert res == (
        ("dash.html",),
        {
            "metas": Markup("METAS"),
            "css": Markup("CSS"),
            "dash_config": Markup("DASH_CONFIG"),
            "scripts": Markup("SCRIPTS"),
            "app_entry": Markup("APP_ENTRY"),
            "renderer": Markup("RENDERER"),
        },
    )
