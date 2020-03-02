from flask_login import UserMixin
from . import db
from datetime import datetime

class User(UserMixin, db.Model):
    id          = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email       = db.Column(db.String(100), unique=True)
    password    = db.Column(db.String(100))
    name        = db.Column(db.String(1000))


class LogonHistory(db.Model):
    '''
    record all attempted logins
    record success/fail of attempted logins
    id, user_id, email, ipaddress, success, date 
    '''
    id          = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    user_id     = db.Column(db.Integer)
    email       = db.Column(db.String(100))
    ipaddress   = db.Column(db.String(15))
    success     = db.Column(db.Boolean)
    date        = db.Column(db.DateTime, default=datetime.utcnow)
