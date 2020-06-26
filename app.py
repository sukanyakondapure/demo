from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify

app = Flask(__name__)

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)



if __name__=='__main__':
    app.run(debug=True)
