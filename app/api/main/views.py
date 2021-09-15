'''Endpoints del API.'''
from flask.views import MethodView
from flask import make_response, jsonify, abort, request
from . import main
from ..dao import QueryGenerator
from ..db import DatabaseManager
from ..team_players import Team
from .errors import not_found, forbidden, not_authorized, bad_request
from .auth import auth_required


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

main.add_url_rule('/api/v1/teams/<string:team_name>', view_func=teams_view,
                  methods=['GET'])

main.add_url_rule('/api/v1/players', view_func=players_view, methods=['GET'])
