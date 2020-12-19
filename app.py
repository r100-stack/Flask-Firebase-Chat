from flask import Flask, render_template
from init_flask import app

# TODO (): Use @app.route to accept GET /
# TODO (): Create a method called index
# TODO (): Have index() return a render_template('index.html')
@app.route('/', methods=['GET'])
def index():
    """GET / - Endpoint to display the homepage HTML file."""

    return render_template('index.html')
