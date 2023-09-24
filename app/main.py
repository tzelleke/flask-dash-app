from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config.Config")
with app.app_context():
    from . import routes  # noqa: F401
    from .dash import crossfilter_example, demo, iris_kmeans

    app = demo.init_dash(app)
    app = iris_kmeans.init_dash(app)
    app = crossfilter_example.init_dash(app)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=8080)
