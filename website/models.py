from website import db
from datetime import datetime



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    salt = db.Column(db.String)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<username: {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    text = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    type_post = db.Column(db.String)  
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project = db.Column(db.Integer, db.ForeignKey('project.id'))
    url = db.Column(db.String, unique=True)
    abs_url = db.Column(db.String, unique=True)#change to be unique
    blurb = db.Column(db.String)
    def __repr__(self):
        return '<Post: {}>'.format(self.title)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    blurb = db.Column(db.String) #acts as TLDR for the project (not just blurb)
    type_project = db.Column(db.String)  
    url = db.Column(db.String, unique=True)
    abs_url = db.Column(db.String, unique=True)
    status = db.Column(db.Integer)
    posts = db.relationship('Post', backref='Project', lazy='dynamic')
    
    def __repr__(self):
        return '<Project: {}>'.format(self.title)
