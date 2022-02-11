from .dash import Dash
from dash import html

app_layout = html.Div(
    children=[html.H1(children="Hello Dash")], className="container-fluid"
)


def init_dash(server):
    dash_app = Dash(server=server, routes_pathname_prefix="/demo/",)
    dash_app.layout = app_layout
    return dash_app.server


if __name__ == "__main__":
    app = Dash(__name__)
    app.run_server(debug=True)
