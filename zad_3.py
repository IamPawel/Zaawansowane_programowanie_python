"""
Endpoint, który zwraca listę filmów w postaci obiektów json. Kroki do
wykonania:
pobrać dane z pliku

- stworzyć klasę Movie (posłuży jako model danych)
- przeiterować pętlą po wierszach z pliku i stworzyć tyle obiektów klasy Movie ile wierszy
- wykorzystać metodę magiczną __dict__ do serializacji obiektu
- zwrócić z metody listę zserializowanych obiektów
    2. Endpoint z filmami przenieść pod adres /movies
    3. Dodać nowe modele dla reszty danych (links, ratings, tags)
    4. Stworzyć pozostałe endpointy dla reszty plików, czyli:
    /links
    /ratings
    /tags
"""

import csv
from fastapi import FastAPI

app = FastAPI()


class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres


class Links:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Ratings:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Tags:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


def read_csv(file_name):
    data = []
    file_path = "database/" + file_name
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Odczytaj nagłówki
        for row in reader:
            # Tworzymy słownik z atrybutami z pierwszego wiersza
            movie_data = {header: value for header, value in zip(headers, row)}
            data.append(movie_data)
    return data


def get_movies():
    movies = read_csv("movies.csv")
    return movies


def get_links():
    links = read_csv("links.csv")
    return [Links(**link) for link in links]


def get_ratings():
    ratings = read_csv("ratings.csv")
    return [Ratings(**rating) for rating in ratings]


def get_tags():
    tags = read_csv("tags.csv")
    return [Tags(**tag) for tag in tags]


@app.get("/movies")
async def movies():
    return get_movies()


@app.get("/links")
async def links():
    return get_links()


@app.get("/ratings")
async def ratings():
    return get_ratings()


@app.get("/tags")
async def tags():
    return get_tags()
