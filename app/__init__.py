from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager  # TODO implement basic login
from flask_admin.contrib.sqla import ModelView
from . import config

import os


app = Flask(__name__)
db = SQLAlchemy(app)


def create_app(config_name="DevelopmentConfig"):
    """
    create an app instance of flask to run a web application

    config_name = the name of a config object inside config.py
    """

    app.config.from_object(config.DevelopmentConfig)

    # Blueprints
    from .user_auth import user_auth
    from .user_views import user_views
    from .admin_auth import admin_auth
    from .admin_views import admin_views

    app.register_blueprint(user_auth, url_prefix="/")
    app.register_blueprint(user_views, url_prefix="/")
    app.register_blueprint(admin_auth, url_prefix="/")
    app.register_blueprint(admin_views, url_prefix="/")

    # user login configuration
    login_manager = LoginManager(app)

    # user loader to load user from database models for login manager
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # any other needed configuration or module
    # ex: csrf_protect(app), db_init(app)
    csrf = CSRFProtect(app)

    # database configuration
    db.init_app(app)
    if not check_database():
        db.create_all()

    return app


def check_database():
    """
    check if database is exist
    """

    if os.path.isfile("database.db"):
        return True
    return False
