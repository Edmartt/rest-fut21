'''Endpoints del API.'''
from flask.views import MethodView
from flask import make_response, jsonify, abort, request, current_app
from . import main
from ..dao import QueryGenerator
from ..db import DatabaseManager
from ..team_players import Team


@main.errorhandler(404)
def not_found(error):
    '''Personaliza la respuesta a JSON en caso de error.'''
    return make_response(jsonify({'Error': 'Not Found'}), 404)


class TeamPlayers(MethodView):

    def __init__(self, team: Team, querygen: QueryGenerator):
        self.team = team
        self.querygen = querygen

    def get(self, team_name: str):
        headers = request.headers
        auth = headers.get('X-Api-Key')  # Capturamos api key enviada por el cliente
        api_key = current_app.config['API_KEY']  # asignamos la variable de entorno como api_key

        if auth == api_key:
            players = self.team.get_players(team_name, self.querygen)

            if players is None:
                abort(404)
            return make_response(jsonify(players), 200)
        return make_response(jsonify({'message': 'Not Authorized'}), 401)


main.add_url_rule('/api/v1/teams/<string:team_name>',
                  view_func=TeamPlayers.as_view
                  ('get_players', Team(), QueryGenerator(DatabaseManager())),
                  methods=['GET'])
