from flask import jsonify

def handle_error(func):
    def try_catch():
        try:
            func()
        except Exception as ex:
            print(ex)
            return jsonify({
                'success': False,
                'error': str(ex)
            }), 422
    return try_catch

def trial_decorator(func):
    name = 'Hello World'
    def trial_inner():
        func(name)
        func(name)
    return trial_inner