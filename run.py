import os
from app.api import create_app

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
