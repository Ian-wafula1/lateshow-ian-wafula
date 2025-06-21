from . import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from . import Appearance

class Guest(db.Model, SerializerMixin):
    
    __tablename__ = 'guests'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)
    
    appearances = db.relationship('Appearance', back_populates='guest', passive_deletes=True)
    episodes = association_proxy('appearances', 'episode', creator=lambda episode: Appearance(episode=episode))