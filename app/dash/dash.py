import dash
from flask import render_template
from markupsafe import Markup


class Dash(dash.Dash):
    def interpolate_index(
        self,
        metas="",
        title="",  # noqa: ARG002
        css="",
        config="",
        scripts="",
        app_entry="",
        favicon="",  # noqa: ARG002
        renderer="",
    ):
        # markupsafe.Markup is used to
        # prevent Jinja from
        # escaping the Dash-rendered markup
        return render_template(
            "dash.html",
            metas=Markup(metas),
            css=Markup(css),
            # config is mapped to dash_config
            # to avoid shadowing the global Flask config
            # in the Jinja environment
            dash_config=Markup(config),
            scripts=Markup(scripts),
            app_entry=Markup(app_entry),
            renderer=Markup(renderer),
        )
