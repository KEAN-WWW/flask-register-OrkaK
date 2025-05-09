"""
Database Initialization and Models
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=True)  # username optional
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, email, password, username=None):
        self.email = email
        self.password = password
        self.username = username

    @classmethod
    def create(cls, email, password):
        return cls(email=email, password=password)

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find_user_by_email(cls, email):
        return cls.query.filter(cls.email == email).first()

    @classmethod
    def find_user_by_id(cls, user_id):
        return cls.query.filter(cls.id == user_id).first()

    @classmethod
    def record_count(cls):
        return cls.query.count()

    def save(self):
        db.session.add(self)
        return db.session.commit()
