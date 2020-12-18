from flask import Flask, jsonify, render_template, request
from init_flask import app, engine
from error_handling import get_connection_and_handle_error

# Endpoint to display the homepage HTML file
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Returns a JSON response with the messages
@app.route('/messages', methods=['GET'])
@get_connection_and_handle_error
def get_messages(*args, **kwargs):
    conn = kwargs['conn']
    results = conn.execute(
        'select ID1, message, sender from messages order by ID desc;')

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

# Adds a message to the database
@app.route('/messages', methods=['POST'])
@get_connection_and_handle_error
def add_message(*args, **kwargs):
    conn = kwargs['conn']

    message = request.json['message']
    sender = request.json['sender']

    conn.execute(
        'insert into messages (message, sender) values (%s, %s);', (message, sender,))

    return jsonify({
        'success': True
    })
