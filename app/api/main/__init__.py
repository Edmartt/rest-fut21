"""Se crea el paquete de la funcionalidad principal de la app."""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import players_views
from . import coincidences_views
