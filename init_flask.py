from flask import Flask
from sqlalchemy import create_engine

import os

# Taking the DB username and password as command line variables to avoid leaking sensitive information in code
username = os.environ['FLASKCHAT_DB_USERNAME']
password = os.environ['FLASKCHAT_DB_PASSWORD']

app = Flask(__name__)

# Database URL that refers to our SQL database
# Engine that we can use to create connections to execute queries
DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user=username, password=password, server='localhost', database='flaskchat')
engine = create_engine(DATABSE_URI)