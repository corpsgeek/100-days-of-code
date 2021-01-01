from flask import Blueprint, request, url_for, render_template, request, jsonify, make_response, redirect
from flask_login import login_user, current_user, login_required
from cblog.models import db, User, Post, Comment 
from cblog.posts.posts_forms import PostForm
from cblog.posts.utils import save_heroimg


post_bp = Blueprint('post_bp', __name__, template_folder = "templates", static_folder = "static")




@post_bp.route("/post", methods = ["GET", "POST"])
@login_required 
def post():
    form = PostForm() 
    legend = "Create Post"

    if form.validate_on_submit():
        #check if form has the image file
        if form.hero.data:
            postimage_file = save_heroimg(form.hero.data)  
            #add the image and other content to the database
            post = Post(title = form.title.data, content = form.content.data, image = postimage_file, author = current_user)
            db.session.add(post)
            db.session.commit() 
            return redirect(url_for('main_bp.index'))
    return render_template("posts/create_post.html", form = form, legend = legend)