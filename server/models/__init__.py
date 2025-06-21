from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

db = SQLAlchemy()

from .Appearance import Appearance
from .Episode import Episode
from .Guest import Guest

__all__ = ['Appearance', 'Episode', 'Guest', 'db']