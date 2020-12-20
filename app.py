from flask import Flask, jsonify, render_template
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