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
    
@api.route('/episodes')
class Episodes(Resource):
    def get(self):
        return [episode.to_dict(rules=('-appearances', '-guests')) for episode in Episode.query.all()]
    
@api.route('/episodes/<int:id>')
class EpisodeByID(Resource):
    
    def get(self, id):
        episode = Episode.query.filter_by(id=id).first()
        if not episode:
            return {'error': 'Episode not found'}, 404
        return make_response(episode.to_dict(), 200)
    
    def delete(self, id):
        episode = Episode.query.filter_by(id=id).first()
        if not episode:
            return {'error': 'Episode not found'}, 404
        db.session.delete(episode)
        db.session.commit()
        return make_response(episode.to_dict(), 200)
    
@api.route('/guests')
class Guests(Resource):
    
    def get(self):
        return [guest.to_dict(rules=('-appearances', '-episodes')) for guest in Guest.query.all()]
    
@api.route('/appearances')
class Appearances(Resource):
    
    def post(self):
        try:
            json = request.get_json()
            appearance = Appearance(rating=json['rating'], episode_id=json['episode_id'], guest_id=json['guest_id'])
            db.session.add(appearance)
            db.session.commit()
            
            return make_response(appearance.to_dict(), 201)
        except:
            return {'errors': ['validation errors']}, 422
        
if __name__ == '__main__':
    app.run(debug=True, port=5555)