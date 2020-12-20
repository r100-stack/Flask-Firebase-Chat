# TODO (1): from flask, also import jsonify
from flask import Flask, jsonify, render_template
from init_flask import app
# TODO (2): from error_handling import get_connection_and_handle_error
from error_handling import get_connection_and_handle_error

@app.route('/', methods=['GET'])
def index():
    """GET / - Endpoint to display the homepage HTML file."""

    return render_template('index.html')

# TODO (3): Use @app.route to create a GET /messages endpoint
# TODO (4): Use the @get_connection_and_handle_error decorator from error_handling.py
# TODO (5): Create a method get_messages(*args, **kwargs)

# TODO (6): Within the method, get the connection that get_connection_and_handle_error gives. ie. conn = kwargs['conn']
# TODO (7): Execute select ID, message, sender from messages order by ID desc;
# TODO (8): Iterate through the records returned and create a list containing all these returned records.
# TODO (9): Each record in the list must be of the form {'ID': row['ID'], 'message': row['message'], 'sender': row['sender']}
# TODO (10): return jsonify {'success': True, messages: messages}

@app.route('/messages', methods=['GET'])
@get_connection_and_handle_error
def get_messages(*args, **kwargs):
    """GET /messages - Returns a JSON response with the messages in the database."""

    conn = kwargs['conn']
    results = conn.execute(
        'select ID, message, sender from messages order by ID desc;')

    messages = []

    for row in results:
        messages.append({
            'ID': row['ID'],
            'message': row['message'],
            'sender': row['sender']
        })

    return jsonify({
        'success': True,
        'messages': messages
    })