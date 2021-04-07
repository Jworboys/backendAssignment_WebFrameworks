import sqlite3
from db import db


class Likes(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, content, user_id):
        self.user_id = user_id

    def json(self):
        return {'user': self.user_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()