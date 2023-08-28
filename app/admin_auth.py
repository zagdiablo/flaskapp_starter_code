"""
for admin authentication process
"""

from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user


admin_auth = Blueprint("admin_auth", __name__)


# TODO test admin login
@admin_auth.route("/admin_login", methods=["GET"])
def admin_login():
    """
    display admin login page
    when /admin_login url is requested using GET method
    and not loged in into any other user or admin account

    return render admin_login.html
    """

    # check if user is loged in
    if current_user.get_id():
        return redirect(url_for("user_views.user_profile"))

    return render_template("admin_templates/admin_login.html")
