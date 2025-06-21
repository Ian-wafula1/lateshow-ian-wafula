from . import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from . import Appearance

class Guest(db.Model, SerializerMixin):
    
    __tablename__ = 'guests'
    
    serialize_rules = ('-appearances.guest','-episodes.guest')
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)
    
    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')
    episodes = association_proxy('appearances', 'episode', creator=lambda episode: Appearance(episode=episode))