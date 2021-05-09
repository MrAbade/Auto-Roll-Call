from os import getenv

from dotenv import load_dotenv


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_DEV_URI")


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_PROD_URI")
    ...


class TestConfig(Config):
    def __new__(cls):
        load_dotenv()
        return super().__new__()

    TESTING = True
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_TEST_URI")


config_selector = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig,
}
