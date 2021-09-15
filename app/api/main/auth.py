from flask import current_app, abort, request


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
