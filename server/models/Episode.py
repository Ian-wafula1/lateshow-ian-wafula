from . import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from . import Appearance

class Episode(db.Model, SerializerMixin):
    
    __tablename__ = 'episodes'
    
    serialize_rules = ('-appearances.episode','-guests.episode')
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)
    
    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')
    guests = association_proxy('appearances', 'guest', creator=lambda guest: Appearance(guest=guest))