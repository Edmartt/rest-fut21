"""Main function which contains the main core"""

from flask import Flask
from config import config
from app.api import db


def create_app(config_name: str):
    """Factory function for a more structured project.

    :params: config_name: A configuration name is required
    for start the application. This name can be:
    1. Development
    2. Testing
    """

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    from app.api.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
