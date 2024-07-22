from typing import Tuple
import pandas as pd
from analitics.core.read_data import movies, ratings, tags


def totals_records(
        table_movies: pd.DataFrame,
        table_ratings: pd.DataFrame,
        table_tags: pd.DataFrame,
) -> Tuple[int, int, int, int]:
    records_movies = table_movies.shape[0]
    records_ratings = table_ratings.shape[0]
    records_tags = table_tags.shape[0]
    records_users = table_ratings.userId.shape[0]
    return records_movies, records_ratings, records_tags, records_users


record_movies, record_ratings, record_tags, record_users = totals_records(movies, ratings, tags)
