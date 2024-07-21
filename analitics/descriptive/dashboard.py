from flask import (
    Flask,
    render_template,
)

from analitics.descriptive.core.config import settings

app = Flask(settings.APP_NAME)


@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    print(f"loading {app.name} ...")
    app.run(debug=True)
