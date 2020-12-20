# TODO (1): from flask, also import request
from flask import Flask, jsonify, render_template, request
from init_flask import app
from error_handling import get_connection_and_handle_error

@app.route('/', methods=['GET'])
def index():
    """GET / - Endpoint to display the homepage HTML file."""

    return render_template('index.html')

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

# TODO (2): Use @app.route to create a POST /messages endpoint
# TODO (3): Use the @get_connection_and_handle_error decorator from error_handling.py
# TODO (4): Create a method add_message(*args, **kwargs)

# TODO (5): Within the method, get the connection that get_connection_and_handle_error gives. ie. conn = kwargs['conn']
# TODO (6): Use request.json[key] to extract the 'message' and 'sender' keys.
# TODO (7): Execute insert into messages (message, sender) values (%s, %s); Here the values are the extracted keys from the request.
# TODO (8): return jsonify {'success': True}

@app.route('/messages', methods=['POST'])
@get_connection_and_handle_error
def add_message(*args, **kwargs):
    """POST /messages - Adds a message to the database."""

    conn = kwargs['conn']

    message = request.json['message']
    sender = request.json['sender']

    conn.execute(
        'insert into messages (message, sender) values (%s, %s);', (message, sender,))

    return jsonify({
        'success': True
    })