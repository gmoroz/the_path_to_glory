import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    DEBUG = True
    SECRET_KEY = "5n6oi67nhhuymazks4mzeh6mb3fklf1"
    TESTING = False

    JSON_AS_ASCII = False
    RESTX_JSON = {
        "ensure_ascii": False,
    }


class Config(BaseConfig):
    STRICT_SLASHES = False
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = "filesystem"
