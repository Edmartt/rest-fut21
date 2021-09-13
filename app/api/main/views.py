'''Endpoints del API.'''
from flask.views import MethodView
from flask import make_response, jsonify, abort, request, current_app
from . import main
from ..dao import QueryGenerator
from ..db import DatabaseManager
from ..team_players import Team


@main.errorhandler(404)
def not_found(error):
    '''Custom answer in json format for 404 error'''
    return make_response(jsonify({'Error': 'Not Found'}), 404)


@main.errorhandler(403)
def forbidden(error):
    '''Custom answer in json format for 403 error'''
    return make_response(jsonify({'Error': 'Forbidden'}), 403)


@main.errorhandler(401)
def not_authorized(error):
    '''Custom answer in json format for 401 error'''
    return make_response(jsonify({'Error': 'Not Authorized'}), 401)


@main.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'Error': 'Bad Request'}), 400)
#  ------------------------------------------------------------------------------


def auth_required(func):
    '''Handles the authentication with header x-api-key.

    Checks if the api_key sent in the header is the same that the one
    in the environment variable.
    '''
    def decorator(*args, **kwargs):
        auth = request.headers.get('X-API-KEY')
        if auth != current_app.config['API_KEY']:
            abort(401)
        return func(*args, **kwargs)
    return decorator


class TeamPlayers(MethodView):
    '''Class representing show_players view function.'''
    decorators = [auth_required]

    def __init__(self, team: Team, querygen: QueryGenerator):
        self.team = team
        self.querygen = querygen

    def get(self, team_name: str):
        players = self.team.get_players(team_name, self.querygen)
        if players is None:
            abort(404)
        return make_response(jsonify(players), 200)


class Coincidences(MethodView):
    '''Class representing get_player view function'''
    decorators = [auth_required]

    def __init__(self, team: Team, querygen: QueryGenerator):
        self.team = team
        self.querygen = querygen

    def get(self):
        args = request.args
        if len(list(args.items())) == 0:  # Innmutable dict turned into list
            abort(400)
        result = self.team.get_player_string(args, self.querygen)
        if result is None:
            abort(404)
        return make_response(jsonify(result), 200)


teams_view = TeamPlayers.as_view('show_players', Team(),
                                 QueryGenerator(DatabaseManager()))

players_view = Coincidences.as_view('get_player', Team(),
                                    QueryGenerator(DatabaseManager()))

main.add_url_rule('/api/v1/teams/<string:team_name>',
                  defaults={'team_name': None}, view_func=teams_view,
                  methods=['GET'])

main.add_url_rule('/api/v1/players', view_func=players_view, methods=['GET'])
