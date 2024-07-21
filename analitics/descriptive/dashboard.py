from flask import (
    Flask,
    render_template,
)

from analitics.descriptive.core.config import settings

app = Flask(settings.APP_NAME)
print(app)
