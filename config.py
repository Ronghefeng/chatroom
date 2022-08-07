import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "hardtohard"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/chat"
    EXPARE_TIME = 604800  # 7 天
    JOBS = []
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_HOST = "localhost"
    REDIS_HOST_PORT = 6379

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI_DEV")
    REDIS_HOST = os.getenv("REDIS_HOST_DEV")
    REDIS_HOST_PORT = os.getenv("REDIS_HOST_PORT")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI_PROD")
    REDIS_HOST = os.getenv("REDIS_HOST_PROD")
    REDIS_HOST_PORT = os.getenv("REDIS_HOST_PORT")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
