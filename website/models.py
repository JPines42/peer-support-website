# Import database and modules
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# User database for account information


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Unique database ID number
    email = db.Column(db.String(150), unique=True)  # Unique Email
    username = db.Column(db.String(150))  # Username
    password = db.Column(db.String(150))  # Password
    date = db.Column(db.DateTime(timezone=True),
                     default=func.now())  # Date of submit
    notes = db.relationship('Note')  # Relationship to Note database

# Notes database for Notes page items


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Database ID number
    data = db.Column(db.String(10000))  # Note data
    date = db.Column(db.DateTime(timezone=True),
                     default=func.now())  # Date of submit
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'))  # ID of user sumbitting note

# FAQ database for FAQ page queries


class Faq(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Database ID number
    email = db.Column(db.String(150))  # Email
    data = db.Column(db.String(10000))  # Inputted data
    date = db.Column(db.DateTime(timezone=True),
                     default=func.now())  # Date of submit
