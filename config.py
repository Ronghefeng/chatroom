# coding = utf-8
"""
@author: zhou
@time:2019/6/20 10:32
"""

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "hardtohard"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/chat"
    EXPARE_TIME = 604800  # 7 天
    JOBS = []
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@online_chat_mysql:3306/chat"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
