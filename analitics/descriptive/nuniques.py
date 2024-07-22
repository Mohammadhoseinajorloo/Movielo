import pandas as pd
from typing import Tuple
from analitics.core.read_data import movies, tags, ratings


def number_of_uniques(
        table_movies: pd.DataFrame,
        table_tags: pd.DataFrame,
        table_ratings: pd.DataFrame,
) -> Tuple[int, int, int, int]:
    um = table_movies.movieId.nunique()
    ut = table_tags.tag.nunique()
    ur = table_ratings.rating.nunique()
    uusr = table_ratings.userId.nunique()
    return um, ut, ur, uusr


unique_movie, unique_tag, unique_rating, unique_user = number_of_uniques(movies, tags, ratings)
