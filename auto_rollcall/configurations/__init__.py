from os import getenv

from flask import Flask


def load_dependecies(app: Flask):
    from auto_rollcall.utils import call_each_init_app_function

    ignore_no_config_files_regex = "^[^_].*[^_].py$"
    path_to_config = "configurations"
    priority_modules_to_config = ["database"]

    call_each_init_app_function(
        app,
        path_to_config,
        priority_modules_to_config,
        ignore_no_config_files_regex,
    )


def init_app(app: Flask):
    from config import config_selector

    config_type = getenv("FLASK_ENV")
    config_obj = config_selector[config_type]
    app.config.from_object(config_obj)
