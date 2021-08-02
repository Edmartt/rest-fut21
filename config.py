"""Valores de configuracion por defecto en la app"""

import os


class Config:

    MYSQL_HOST = os.environ.get('DB_HOST')
    MYSQL_USER = os.environ.get('DB_USERNAME')
    MYSQL_PASSWORD = os.environ.get('DB_PASSWORD')
    MYSQL_DB = os.environ.get('DB_NAME')
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
