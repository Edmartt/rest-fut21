"""Valores de configuracion por defecto en la app"""

import os


class Config:

    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
    API_KEY = os.environ.get('API_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    DEBUG = True


config = {
        'development': DevelopmentConfig,
        'default': DevelopmentConfig
        }
