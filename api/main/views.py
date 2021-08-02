from flask import make_response, jsonify, abort, request
from . import main
from ..team_players import Team


@main.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not Found'}), 404)


@main.route('/api/v1/team/<string:name>', methods=['GET'])
def get_team_players(name):
    team = Team()

    players = team.get_players(name)
    if players is None:
        abort(404)
    return make_response(jsonify(players), 200)


@main.route('/api/v1/players')
def get_data():

    args = request.args
    team = Team()
    result = team.get_player_string(args)

    if result is None:
        abort(404)
    return make_response(jsonify(result), 200)
