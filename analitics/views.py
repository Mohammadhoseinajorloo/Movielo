from flask import render_template
from analitics.descriptive.totals import record_users, record_ratings, record_movies, record_tags
from analitics.descriptive.nuniques import unique_tag, unique_movie, unique_rating, unique_user
from analitics.descriptive.means import mean_users, mean_movies, mean_ratings, mean_tags


def home():
    return render_template("home.html")


def dashboard():
    return render_template(
        "dashboard.html",
        all_user=record_users,
        all_ratings=record_ratings,
        all_movies=record_movies,
        all_tags=record_tags,
        # __________________________
        unique_user=unique_user,
        unique_movie=unique_movie,
        unique_tag=unique_tag,
        unique_ratings=unique_rating,
        # ________________________________
        mean_users=mean_users,
        mean_movies=mean_movies,
        mean_ratings=mean_ratings,
        mean_tags=mean_tags,
    )
