"""
authentication related function
"""

from flask import Blueprint, render_template


auth = Blueprint("auth", __name__)


# add route API below as needed
# ex: login authentication
@auth.route("/login", methods=["GET"])
def login():
    return render_template("<h1>Hello World</h1>")
