from flask import render_template


def home():
    return render_template("home.html")


def dashboard():
    return render_template("dashboard.html")
