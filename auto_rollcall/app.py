from flask import Flask

from auto_rollcall import configurations
from auto_rollcall.configurations import database
from auto_rollcall.configurations import migration


def create_app():
    app = Flask(__name__)

    configurations.init_app(app)
    database.init_app(app)
    migration.init_app(app)

    return app
