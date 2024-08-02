from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#User database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #Database ID number
    email = db.Column(db.String(150), unique=True) #Email
    username = db.Column(db.String(150)) #Username
    password = db.Column(db.String(150)) #Password
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #Date of submit
    notes = db.relationship('Note')

#Notes database
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Database ID number
    data = db.Column(db.String(10000)) #Inputted data
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #Date of submit
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #User ID number

#FAQ database
class Faq(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Database ID number
    email = db.Column(db.String(150)) #Email
    data = db.Column(db.String(10000)) #Inputted data
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #Date of submit
