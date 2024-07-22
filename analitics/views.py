from flask import render_template


def home():
    return render_template("home.html")


def dashboard():
    total_data = 0
    null_data = 0
    total_users= 0
    total_movies= 0
    return render_template(
        "dashboard.html",
        total_data=total_data,
        null_data=null_data,
        total_users=total_users,
        total_movies=total_movies
    )
