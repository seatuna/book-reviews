import pandas as pd


def get_book_genres():
    books = pd.read_csv("../data/top-100-trending-books.csv")
    all_genres = set()
    for genre_list in books.genre.unique():
        for genre in genre_list.split(","):
            all_genres.add(genre.strip())
    return all_genres


if __name__ == "__main__":
    get_book_genres()
