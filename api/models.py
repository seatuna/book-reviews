from sqlalchemy import inspect
from api import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer)
    title = db.Column(db.String())
    price = db.Column(db.Numeric)
    author = db.Column(db.String())
    pub_year = db.Column(db.DateTime)
    genres = db.relationship(
        "Genre", backref="book", cascade="all, delete, delete-orphan"
    )
    link_url = db.Column(db.String())
    thumbnail_url = db.Column(db.String())

    def __init__(self, url, result_all):
        self.url = url
        self.result_all = result_all

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r>" % self.id


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String())
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))

    def __init__(self, genre_name, result_all):
        self.genre_name = genre_name
        self.result_all = result_all

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return "<%r>" % self.genre_name
