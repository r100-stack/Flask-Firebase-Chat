from flask import Flask, jsonify, render_template, request, redirect
from sqlalchemy import create_engine
from data import sample_messages

app = Flask(__name__)
engine = create_engine('mysql://kali:kali@localhost:3306/flaskchat')
conn = engine.connect()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sample_messages')
def get_sample_messages():
    return jsonify(sample_messages)

@app.route('/messages', methods=['GET'])
def get_messages():
    results = conn.execute("select * from messages order by id desc;")
    messages = []
    for row in results:
        messages.append({
            'id': row['id'],
            'message': row['message'],
            'sender': row['sender']
        })
    return jsonify(messages)

@app.route('/messages', methods=['POST'])
def post_message():
    conn.execute('insert into messages (message, sender) values (%s, %s)', (request.get_json()['message'], request.get_json()['sender']))
    return redirect('/messages')

