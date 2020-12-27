from flask import Blueprint, request, url_for, render_template
from flask_login import login_user, current_user, login_required
from cblog.models import db, User, Post, Comment 
from cblog.posts.posts_forms import PostForm
post_bp = Blueprint('post_bp', __name__, template_folder = "templates", static_folder = "static")


@post_bp.route("/post", methods = ["GET", "POST"])
@login_required 
def post():
    form = PostForm()
    return render_template("posts/create_post.html", form = form)