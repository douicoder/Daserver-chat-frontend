from flask import Blueprint, render_template, session, redirect, url_for

chat_bp = Blueprint("chat", __name__)


def login_required(f):
    from functools import wraps

    @wraps(f)
    def decorated(*args, **kwargs):
        if "access_token" not in session:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated


@chat_bp.route("/chat")
@login_required
def index():
    user = session.get("user", {})
    return render_template("chat.html", user=user)


@chat_bp.route("/admin")
@login_required
def admin_page():
    user = session.get("user", {})
    if not user.get("is_admin"):
        return redirect(url_for("chat.index"))
    return render_template("admin.html", user=user)
