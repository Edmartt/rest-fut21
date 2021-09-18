from . import main
from flask import make_response, jsonify


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


@main.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'Error': 'Internal Server Error'}))
