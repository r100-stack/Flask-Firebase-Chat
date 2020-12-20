# TODO (1): from flask import Flask
# TODO (2): from sqlalchemy import create_engine
from flask import Flask
from sqlalchemy import create_engine

# TODO (3): import os
import os

# Taking the DB username and password as command line variables to avoid leaking sensitive information in code
# TODO (4): Create a "username" with the FLASKCHAT_DB_USERNAME environment variable
# TODO (5): Create a "password" with the FLASKCHAT_DB_PASSWORD environment variable
username = os.environ['FLASKCHAT_DB_USERNAME']
password = os.environ['FLASKCHAT_DB_PASSWORD']

# TODO (6): Create a definition for the Flask app.
app = Flask(__name__)

# Database URL that refers to our SQL database
# TODO (7): Create a "DATABASE_URI" for the MySQL database
# Engine that we can use to create connections to execute queries
# TODO (8): Create an "engine" using the above DATABASE_URI
DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user=username, password=password, server='localhost', database='flaskchat')
engine = create_engine(DATABSE_URI)