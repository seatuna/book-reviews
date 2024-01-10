from flask import jsonify
from .models import Book, Genre


def list_all_books():
    books = Book.query.all()
    response = []
    for book in books:
        response.append(book.to_dict())
    return jsonify(response)


def list_all_genres():
    genres = Genre.query.all()
    response = []
    for genre in genres:
        response.append(genre.to_dict())
    return jsonify(response)
