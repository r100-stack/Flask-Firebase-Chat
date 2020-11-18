from flask import Flask, jsonify, render_template, request, redirect
# from flask_mysqldb import MySQL
from sqlalchemy import create_engine
from data import sample_messages

app = Flask(__name__)
engine = create_engine('mysql://kali:kali@localhost:3306/flaskchat')
conn = engine.connect()
# app.config['SQLALCHEMY_DATABASE_URI'] = ''

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sample_messages')
def get_sample_messages():
    return jsonify(sample_messages)

@app.route('/messages', methods=['GET'])
def get_messages():
    results = conn.execute("select * from messages;")
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
    # print('here');
    # print(request.form['message'], request.form['sender'])
    conn.execute('insert into messages (message, sender) values (%s, %s)', (request.form['message'], request.form['sender']))
    return redirect('/')

