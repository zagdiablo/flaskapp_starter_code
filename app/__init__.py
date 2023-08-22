from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager  # TODO implement basic login
from flask_admin import Admin  # TODO implement basic admin
from flask_admin.contrib.sqla import ModelView
from . import config


app = Flask(__name__)
db = SQLAlchemy(app)


def create_app(config_name="DevelopmentConfig"):
    """
    create an app instance of flask to run a web application

    config_name = the name of a config object inside config.py
    """

    app.config.from_object(config.DevelopmentConfig)

    # database configuration
    db.init_app(app)
    db.create_all()

    # Blueprints
    from .auth import auth

    app.register_blueprint(auth, url_prefix="/")

    # user login configuration
    login_manager = LoginManager(app)

    # admin page configuration
    from .models import User

    admin = Admin(app, name="Admin Panel", template_mode="bootstrap3")
    admin.add_view(ModelView(User, db.session))

    # user loader to load user from database models for login manager
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # any other needed configuration or module
    # ex: csrf_protect(app), db_init(app)
    csrf = CSRFProtect(app)

    # register blueprints

    return app
