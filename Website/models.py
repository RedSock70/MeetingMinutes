from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    subject = db.Column(db.String(32))
    absents = db.Column(db.String(32))
    raisedby = db.Column(db.String(32))
    actions = db.Column(db.String(1000))
    tobea = db.Column(db.String(1000))
    subsequent = db.Column(db.String(1000))
    completion = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    FirstName = db.Column(db.String(150))
    notes = db.relationship('Note')



#from .  import db 
#from flask_login import UserMixin
#from sqlalchemy.sql import func

#class Note(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    data = db.Column(db.String(10000))
#    date = db.Column(db.DateTime(timezone=True), default=func.now())
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


#class User(db.Model, UserMixin):
#    id = db.Column(db.Integer, primary_key=True)
#    email = db.Column(db.string(150), unique=True)
#    password = db.Column(db.String(150))
#    first_name = db.Column(db.String(150))
