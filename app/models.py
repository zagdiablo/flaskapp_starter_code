"""
create a database models
"""
from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    """
    basic user model with username, password, and role to define its role: admin, staff, or user
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Boolean, nullable=False, default="user")
