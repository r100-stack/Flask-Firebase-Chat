from flask import Flask, jsonify, render_template, request
from init_flask import app, engine

# Endpoint to display the homepage HTML file
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Returns a JSON response with the messages
@app.route('/messages', methods=['GET'])
def get_messages():
    try:
        conn = engine.connect()
        results = conn.execute('select ID, message, sender from messages order by ID desc;')

        messages = []

        for row in results:
            messages.append({
                'ID': row['ID'],
                'message': row['message'],
                'sender': row['sender']
            })

        conn.close()

        return jsonify({
            'success': True,
            'messages': messages
        })
    except Exception as ex:
        print(ex)
        return jsonify({
            'success': False,
            'error': str(ex)
        }), 422

# Adds a message to the database
@app.route('/messages', methods=['POST'])
def add_message():
    try:
        conn = engine.connect()

        message = request.json['message']
        sender = request.json['sender']

        conn.execute('insert into messages (message, sender) values (%s, %s);', (message, sender,))

        conn.close()

        return jsonify({
            'success': True
        })
    except Exception as ex:
        print(ex)
        return jsonify({
            'success': False
        }), 422
