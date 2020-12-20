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

@app.route('/messages', methods=['DELETE'])
@get_connection_and_handle_error
def delete_message(*args, **kwargs):
    """DELETE /messages - Deletes a message from the database."""

    conn = kwargs['conn']

    ID = request.json['ID']

    conn.execute('delete from messages where ID=%s;', (ID,))

    return jsonify({
        'success': True
    })

@app.route('/messages', methods=['PATCH'])
@get_connection_and_handle_error
def edit_message(*args, **kwargs):
    """PATCH /messages - Edits a message in the database."""

    conn = kwargs['conn']

    ID = request.json['ID']
    message = request.json['message']

    conn.execute('update messages set message=%s where ID=%s;', (message, ID,))

    return jsonify({
        'success': True
    })
