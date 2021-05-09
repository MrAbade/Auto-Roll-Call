from flask import Flask

from auto_rollcall import configurations


def simple_app() -> Flask:
    app_name = __name__.split(".")[0]
    app = Flask(app_name)
    configurations.init_app(app)
    return app


def create_app():
    app = simple_app()
    configurations.load_dependecies(app)
    return app
