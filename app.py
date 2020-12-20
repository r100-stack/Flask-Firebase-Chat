from flask import Flask, render_template
from init_flask import app

@app.route('/', methods=['GET'])
def index():
    """GET / - Endpoint to display the homepage HTML file."""

    return render_template('index.html')
