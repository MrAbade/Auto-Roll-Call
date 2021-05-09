from flask import Flask
from flask_sqlalchemy import BaseQuery, SQLAlchemy
from flask_sqlalchemy.model import Model

from auto_rollcall.utils.patterns import Singleton


class Database(SQLAlchemy, metaclass=Singleton):
    def __init__(
        self,
        app=None,
        use_native_unicode=True,
        session_options=None,
        metadata=None,
        query_class=BaseQuery,
        model_class=Model,
        engine_options=None,
    ):
        super().__init__(
            app=app,
            use_native_unicode=use_native_unicode,
            session_options=session_options,
            metadata=metadata,
            query_class=query_class,
            model_class=model_class,
            engine_options=engine_options,
        )


def init_app(app: Flask, db: Database = Database()):
    db.init_app(app)
    app.db = db
