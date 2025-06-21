from . import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

class Appearance(db.Model, SerializerMixin):
    
    __tablename__ = 'appearances'
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id', ondelete='CASCADE'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id', ondelete='CASCADE'), nullable=False)
    
    episode = db.relationship('Episode', back_populates='appearances')
    guest = db.relationship('Guest', back_populates='appearances')
    
    @validates('rating')
    def validate_rating(self, key, rating):
        if rating < 1 or rating > 5:
            raise ValueError('Rating must be between 1 and 5')
        return rating
