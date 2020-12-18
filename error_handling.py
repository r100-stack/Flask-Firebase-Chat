from flask import jsonify
from init_flask import engine

def get_connection_and_handle_error(func):
    def try_catch():
        try:
            conn = engine.connect()
            response = func(conn=conn)
        except Exception as ex:
            print(ex)
            response = jsonify({
                'success': False,
                'error': str(ex)
            }), 500
        finally:
            conn.close()
        return response
    try_catch.__name__ = func.__name__
    return try_catch

def trial_decorator(func):
    name = 'Hello World'
    def trial_inner():
        func(name)
        func(name)
    return trial_inner