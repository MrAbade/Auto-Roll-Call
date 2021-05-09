from os import getenv

from flask import Flask


def init_app(app: Flask):
    from config import config_selector

    config_type = getenv("FLASK_ENV")
    config_obj = config_selector[config_type]
    app.config.from_object(config_obj)
