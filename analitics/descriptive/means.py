import pandas as pd
from typing import Tuple
from analitics.core.read_data import movies, tags, ratings


def mean_of_fields(
        table_movies: pd.DataFrame,
        table_tags: pd.DataFrame,
        table_ratings: pd.DataFrame,
) -> Tuple[int, str, int, int]:
    mm = round(table_movies.movieId.mean(), 2)
    mt = table_tags.tag.mode().values[0]
    mu = round(table_ratings.userId.mean(), 2)
    mr = round(table_ratings.rating.mean(), 2)
    return mm, mt, mu, mr


mean_movies, mean_tags, mean_users, mean_ratings = mean_of_fields(movies, tags, ratings)
