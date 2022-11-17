from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
moment = Moment()
boot = Bootstrap()
mail = Mail()


def create_app(config_name: str) -> Flask:
    """
    A function to create an d instance of flask app
    :param config_name: [dev, test, prod, default]
    :return: Flask instance
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    moment.init_app(app)
    boot.init_app(app)
    mail.init_app(app)

    # import blueprints
    from app.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
