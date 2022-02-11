from flask import current_app as app
from flask import render_template
import markdown
import markdown.extensions.fenced_code
from pygments.formatters.html import HtmlFormatter
from markupsafe import Markup


@app.route("/")
def index():
    with open("README.md", "r") as fp:
        formatter = HtmlFormatter(
            style="solarized-dark", full=True, cssclass="codehilite",
        )
        styles = f"<style>{formatter.get_style_defs()}</style>"
        html = (
            markdown.markdown(fp.read(), extensions=["codehilite", "fenced_code"])
            .replace(
                # Fix relative path for image(s) when rendering README.md on index page
                'src="app/',
                'src="',
            )
            .replace("codehilite", "codehilite p-2 mb-3 bg-dark")
        )
        return render_template(
            "index.html", content=Markup(html), styles=Markup(styles),
        )
