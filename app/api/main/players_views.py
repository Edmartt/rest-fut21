'''Endpoints del API.'''
from flask.views import MethodView
from flask import make_response, jsonify, abort
from . import main
from ..dao import QueryGenerator
from ..db import DatabaseManager
from ..team_players import Team
from .errors import not_found, forbidden, not_authorized, bad_request, \
        internal_server_error
from .auth import auth_required


class TeamPlayers(MethodView):
    '''Class representing show_players in team http methods.'''
    decorators = [auth_required]

    def __init__(self, team: Team, querygen: QueryGenerator):
        self.team = team
        self.querygen = querygen

    def get(self, team_name: str):
        players = self.team.get_players(team_name, self.querygen)
        if players is None:
            abort(404)
        return make_response(jsonify(players), 200)


# Generates the view function executed when a get request is made
teams_view = TeamPlayers.as_view('show_players', Team(),
                                 QueryGenerator(DatabaseManager()))

# Endpoint definition
main.add_url_rule('/api/v1/teams/<string:team_name>', view_func=teams_view,
                  methods=['GET'])
