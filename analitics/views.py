from flask import render_template


def home():
    return render_template("home.html")


def dashboard():
    total_data = 100000
    return render_template("dashboard.html", total_data=total_data)
