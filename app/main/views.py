#################################################
#  File to handler different routes of the app  #
#################################################

from flask import render_template

# import models
# from app.models import ...
# import blueprints
from . import main


@main.route("/")
def index():
    return render_template("client/index.html"), 200
