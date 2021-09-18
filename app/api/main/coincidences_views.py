from flask.views import MethodView
from flask import make_response, jsonify, abort, request
from . import main
from ..dao import QueryGenerator
from ..db import DatabaseManager
from ..team_players import Team
from .errors import not_found, forbidden, not_authorized, bad_request,\
        internal_server_error
from .auth import auth_required


class Coincidences(MethodView):
    '''Class representing get_player coincidences http methods'''
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


# Generates the view function executed when a get request is made
players_view = Coincidences.as_view('get_player', Team(),
                                    QueryGenerator(DatabaseManager()))

# Endpoint definition
main.add_url_rule('/api/v1/players', view_func=players_view, methods=['GET'])
