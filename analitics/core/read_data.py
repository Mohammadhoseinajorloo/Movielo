from .config import settings
from pandas import read_csv


def read_data(base_path: str):
    movies = read_csv(f"{base_path}/movies.csv")
    ratings = read_csv(f"{base_path}/ratings.csv")
    tags = read_csv(f"{base_path}/tags.csv")
    links = read_csv(f"{base_path}/links.csv")
    return movies, ratings, tags, links


movies, ratings, tags, links = read_data(settings.DATA_DIR)
