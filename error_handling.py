from flask import jsonify
from init_flask import engine


def get_connection_and_handle_error(func):
    """Python decorator to do a try catch.
    On success returns http response 200.
    On failure returns http response 500."""

    def try_catch():
        try:
            # TODO (1): Create a db connection using engine.connect(). Name it conn.
            # TODO (2): Call the passed func parameter. Give it conn=conn as a parameter.
            # TODO (3): response = output of func(conn=conn)
            conn = engine.connect()
            response = func(conn=conn)
        except Exception as ex:
            print(ex)
            # TODO (4): response = jsonify( {'success': False, 'error': str(ex)} )
            # TODO (5): response must have HTTP response code 500.
            response = jsonify({
                'success': False,
                'error': str(ex)
            }), 500
        finally:
            # TODO (6): Close the connection using conn.close()
            conn.close()
        # TODO (7): Return the variable "response"
        return response
    try_catch.__name__ = func.__name__
    return try_catch
