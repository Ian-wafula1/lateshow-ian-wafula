from flask import Flask, make_response, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restx import Api, Resource
from models import db, Appearance, Guest, Episode

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)
api = Api(app)
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=5555)