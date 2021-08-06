'''Endpoints del API.'''

from flask import make_response, jsonify, abort, request, current_app
from . import main
from ..team_players import Team


@main.errorhandler(404)
def not_found(error):
    '''Personaliza la respuesta a JSON en caso de error.'''
    return make_response(jsonify({'Error': 'Not Found'}), 404)


@main.route('/api/v1/team/<string:name>', methods=['GET'])
def get_team_players(name: str):
    '''Obtiene los jugadores de un equipo.'''

    headers = request.headers
    auth = headers.get('X-Api-Key')  # Capturamos api key enviada por el cliente
    api_key = current_app.config['API_KEY']  # asignamos la variable de entorno como api_key
    team = Team()

    if auth == api_key:
        players = team.get_players(name)

        if players is None:
            abort(404)
        return make_response(jsonify(players), 200)

    return make_response(jsonify({'message': 'Not Authorized'}), 401)


@main.route('/api/v1/players')
def get_data():
    '''Busca jugadores con coincidencias parciales o totales.

    Acepta querystrings: search="nombre de jugador"&order.
    El orden puede ser asc o desc, por defecto es asc, incluso si se omite.
    '''
    args = request.args
    team = Team()
    result = team.get_player_string(args)
    headers = request.headers
    auth = headers.get('X-Api-Key')
    api_key = current_app.config['API_KEY']

    if auth == api_key:
        if result is None:
            abort(404)
        return make_response(jsonify(result), 200)

    return make_response(jsonify({'message': 'Not Authorized'}), 401)
