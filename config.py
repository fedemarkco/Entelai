import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret_key")
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
