from flask import render_template
from analitics.descriptive.totals import record_users, record_ratings, record_movies, record_tags


def home():
    return render_template("home.html")


def dashboard():
    return render_template(
        "dashboard.html",
        all_user=record_users,
        all_ratings=record_ratings,
        all_movies=record_movies,
        all_tags=record_tags,
    )
