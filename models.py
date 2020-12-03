from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(),  primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    avatar = db.Column(db.String(20), nullable=False, default='pic.jpg')
    password = db.Column(db.String(20), nullable=False)