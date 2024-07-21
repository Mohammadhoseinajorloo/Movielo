from flask import (
    Flask,
    render_template,
)

from analitics.descriptive.core.config import settings

app = Flask(settings.APP_NAME)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)