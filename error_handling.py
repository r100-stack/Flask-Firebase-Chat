from flask import jsonify
from init_flask import engine


def get_connection_and_handle_error(func):
    """Python decorator to do a try catch.
    On success returns http response 200.
    On failure returns http response 500."""

    return None
