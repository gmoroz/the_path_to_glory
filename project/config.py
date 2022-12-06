class BaseConfig:
    DEBUG = True
    SECRET_KEY = "249y823r9v8238r9u"
    TESTING = False

    JSON_AS_ASCII = False
    RESTX_JSON = {
        "ensure_ascii": False,
    }


class Config(BaseConfig):
    pass
