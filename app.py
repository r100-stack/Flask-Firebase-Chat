# TODO (1): Import the necessary libraries

from flask import Flask, jsonify, render_template, request, redirect
from sqlalchemy import create_engine
from data import sample_messages

# TODO (2): Setup the app, engine, and connection

app = Flask(__name__)
engine = create_engine('mysql://kali:kali@localhost:3306/flaskchat')
conn = engine.connect()

# TODO (3): Render the index.html template for the / endpoint

@app.route('/')
def index():
    return render_template("index.html")

# TODO (4): Return the sample messages as a json for the /sample_messages endpoint

@app.route('/sample_messages')
def get_sample_messages():
    return jsonify(sample_messages)

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify('')

@app.route('/messages', methods=['POST'])
def post_message():
    return jsonify('')

