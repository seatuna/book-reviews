import numpy as np
import pandas as pd


def get_book_genres():
    books = pd.read_csv("data/top-100-trending-books.csv")
    books.head()


if __name__ == "__main__":
    print(get_book_genres())
