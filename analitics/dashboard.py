from flask import (
    Flask,
    render_template,
)

from analitics.core.config import settings

app = Flask(settings.APP_NAME)


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    print(f"loading analitic website {app.name} ...")
    app.run(debug=True)
