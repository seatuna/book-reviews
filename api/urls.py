from flask import request

from .app import app
from .controllers import list_all_books, list_all_genres


@app.route("/books", methods=["GET"])
def list_books():
    if request.method == "GET":
        return list_all_books()
    else:
        return "Method is Not Allowed"


@app.route("/genres", methods=["GET"])
def list_genres():
    if request.method == "GET":
        return list_all_genres()
    else:
        return "Method is Not Allowed"
