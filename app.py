# TODO (5): from flask import Flask, render_template
# TODO (6): from init_flask import app
from flask import Flask, render_template
from init_flask import app

# TODO (7): Use @app.route to accept GET /
# TODO (8): Create a method called index
# TODO (9): Have index() return a render_template('index.html')
@app.route('/', methods=['GET'])
def index():
    """GET / - Endpoint to display the homepage HTML file."""

    return render_template('index.html')
