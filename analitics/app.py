import views
from flask import Flask

from analitics.core.config import settings

app = Flask(settings.APP_NAME)

app.add_url_rule("/", methods=["GET"], view_func=views.home)
app.add_url_rule("/dashboard", methods=["GET"], view_func=views.dashboard)

if __name__ == "__main__":
    print(f"loading analitic website {app.name} ...")
    app.run(debug=True)
