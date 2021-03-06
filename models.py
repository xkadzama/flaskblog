from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
# from main_app import login_manager

db = SQLAlchemy()

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(),  primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    avatar = db.Column(db.String(20), nullable=False, default='pic.jpg')
    password = db.Column(db.String(20), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return self.username

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    content = db.Column(db.Text(), nullable=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=True)

    def __repr__(self):
        return self.title